# Code snippet taken directly and edited from the DDNet codebase.
# Teeworlds Copyright (C) 2007-2014 Magnus Auvinen
# DDRace    Copyright (C) 2010-2011 Shereef Marzouk
# DDNet     Copyright (C) 2013-2022 Dennis Felsing

GlobalIdCounter = 0
def GetID():
	global GlobalIdCounter
	GlobalIdCounter += 1
	return GlobalIdCounter
def GetUID():
	return f"x{int(GetID())}"

def FixCasing(Str):
	NewStr = ""
	NextUpperCase = True
	for c in Str:
		if NextUpperCase:
			NextUpperCase = False
			NewStr += c.upper()
		else:
			if c == "_":
				NextUpperCase = True
			else:
				NewStr += c.lower()
	return NewStr

def FormatName(typ, name):
	if "*" in typ:
		return "m_p" + FixCasing(name)
	if "[]" in typ:
		return "m_a" + FixCasing(name)
	return "m_" + FixCasing(name)

class BaseType:
	def __init__(self, type_name):
		self._type_name = type_name
		self._target_name = "INVALID"
		self._id = GetID() # this is used to remember what order the members have in structures etc

	def Identifier(self):
		return "x"+str(self._id)
	def TargetName(self):
		return self._target_name
	def TypeName(self):
		return self._type_name
	def ID(self):
		return self._id

	def EmitDeclaration(self, name):
		return [f"{self.TypeName()} {FormatName(self.TypeName(), name)};"]
	def EmitPreDefinition(self, target_name):
		self._target_name = target_name
		return []
	def EmitDefinition(self, _name):
		return []

class MemberType:
	def __init__(self, name, var):
		self.name = name
		self.var = var

class Struct(BaseType):
	def __init__(self, type_name):
		BaseType.__init__(self, type_name)
	def Members(self):
		def sorter(a):
			return a.var.ID()
		m = []
		for name, value in self.__dict__.items():
			if name[0] == "_":
				continue
			m += [MemberType(name, value)]
		m.sort(key = sorter)
		return m

	def EmitTypeDeclaration(self, _name):
		lines = []
		lines += ["struct " + self.TypeName()]
		lines += ["{"]
		for member in self.Members():
			lines += ["\t"+l for l in member.var.EmitDeclaration(member.name)]
		lines += ["};"]
		return lines

	def EmitPreDefinition(self, target_name):
		BaseType.EmitPreDefinition(self, target_name)
		lines = []
		for member in self.Members():
			lines += member.var.EmitPreDefinition(target_name+"."+member.name)
		return lines
	def EmitDefinition(self, _name):
		lines = [f"/* {self.TargetName()} */ {{"]
		for member in self.Members():
			lines += ["\t" + " ".join(member.var.EmitDefinition("")) + ","]
		lines += ["}"]
		return lines

class Array(BaseType):
	def __init__(self, typ):
		BaseType.__init__(self, typ.TypeName())
		self.type = typ
		self.items = []
	def Add(self, instance):
		if instance.TypeName() != self.type.TypeName():
			raise ValueError("bah")
		self.items += [instance]
	def EmitDeclaration(self, name):
		return [f"int m_Num{FixCasing(name)};",
			f"{self.TypeName()} *{FormatName('[]', name)};"]
	def EmitPreDefinition(self, target_name):
		BaseType.EmitPreDefinition(self, target_name)

		lines = []
		i = 0
		for item in self.items:
			lines += item.EmitPreDefinition(f"{self.Identifier()}[{int(i)}]")
			i += 1

		if self.items:
			lines += [f"static {self.TypeName()} {self.Identifier()}[] = {{"]
			for item in self.items:
				itemlines = item.EmitDefinition("")
				lines += ["\t" + " ".join(itemlines).replace("\t", " ") + ","]
			lines += ["};"]
		else:
			lines += [f"static {self.TypeName()} *{self.Identifier()} = 0;"]

		return lines
	def EmitDefinition(self, _name):
		return [str(len(self.items))+","+self.Identifier()]

# Basic Types

class Int(BaseType):
	def __init__(self, value):
		BaseType.__init__(self, "int")
		self.value = value
	def Set(self, value):
		self.value = value
	def EmitDefinition(self, _name):
		return [f"{int(self.value)}"]
		#return ["%d /* %s */"%(self.value, self._target_name)]

class Float(BaseType):
	def __init__(self, value):
		BaseType.__init__(self, "float")
		self.value = value
	def Set(self, value):
		self.value = value
	def EmitDefinition(self, _name):
		return [f"{self.value:f}f"]
		#return ["%d /* %s */"%(self.value, self._target_name)]

class String(BaseType):
	def __init__(self, value):
		BaseType.__init__(self, "const char*")
		self.value = value
	def Set(self, value):
		self.value = value
	def EmitDefinition(self, _name):
		return ['"'+self.value+'"']

class Pointer(BaseType):
	def __init__(self, typ, target):
		BaseType.__init__(self, f"{typ().TypeName()}*")
		self.target = target
	def Set(self, target):
		self.target = target
	def EmitDefinition(self, _name):
		return ["&"+self.target.TargetName()]

class TextureHandle(BaseType):
	def __init__(self):
		BaseType.__init__(self, "IGraphics::CTextureHandle")
	def EmitDefinition(self, _name):
		return ["IGraphics::CTextureHandle()"]

# helper functions

def EmitTypeDeclaration(root):
	for l in root().EmitTypeDeclaration(""):
		print(l)

def EmitDefinition(root, name):
	for l in root.EmitPreDefinition(name):
		print(l)
	print(f"{root.TypeName()} {name} = ")
	for l in root.EmitDefinition(name):
		print(l)
	print(";")

# Network stuff after this

class Enum:
	def __init__(self, name, values):
		self.name = name
		self.values = values

