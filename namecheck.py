import os, sys

def checkDuplicates(name):
  if os.path.exists(name) == False:
    return name

  duplicates = 1
  while os.path.exists(name + "-({})".format(duplicates)) == True and duplicates < 16:
      duplicates += 1

  if duplicates >= 16:
    sys.exit("{} has too many duplicate names. Please rename your folder to something different.".format(sys.argv[1]))
  else:
    return name + "-({})".format(duplicates)