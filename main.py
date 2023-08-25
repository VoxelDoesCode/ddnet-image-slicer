from PIL import Image
import os, sys

import content

set_images = content.container.images.items
set_spritesets = content.container.spritesets.items
set_sprites = content.container.sprites.items

folders_list = ["weapons", "particles", "map_items", "hud", "gui", "emoticons"]
images_list = []

print("images ~ " + str(len(set_images)))
print("spritesets ~ " + str(len(set_spritesets)))
print("sprites ~ " + str(len(set_sprites)))
print("------------")

for index in range(len(set_images)):
  imageIndex = set_images[index]

  imageName = imageIndex.name.value
  imageFilename = imageIndex.filename.value

  print(index, imageFilename)

  if imageName == "null":
    images_list.append("NULL")
    index += 1
    continue

  divX = set_spritesets[index].gridx.value
  divY = set_spritesets[index].gridy.value

  try:
    images_list.append(Image.open("images/" + imageFilename))
  except:
    print("You are missing " + str(imageFilename) + ". A copy is located inside the images folder, or inside DDNet's data folder.")
    break

  width, height = images_list[index].size

  if width == 0 or width % divX != 0 or height == 0 or height % divY != 0:
    print("The width of texture {} is not divisible by {}, or the height is not divisible by {}, which might cause visual bugs.".format(imageName, divX, divY))

for index in folders_list:
  newPath = "images/split/" + index
  os.makedirs(newPath)

for index in range(len(set_sprites)):
  spriteIndex = set_sprites[index]

  if spriteIndex.w.value == 0 or spriteIndex.h.value == 0:
    continue

  currentImage = set_spritesets.index(spriteIndex.set.target)
  imageName = spriteIndex.set.target.image.target.filename.value

  if set_spritesets[currentImage].gridx.value == 1 or set_spritesets[currentImage].gridy.value == 1:
      try:
        images_list[currentImage].save("images/split/{}/{}".format(spriteIndex.location.value, imageName))
      except:
        print("{} failed to export.".format(imageName))
        break
      continue

  width, height = images_list[currentImage].size

  divX = width / set_spritesets[currentImage].gridx.value
  divY = height / set_spritesets[currentImage].gridy.value

  cropX = spriteIndex.x.value * divX
  cropY = spriteIndex.y.value * divY
  cropWidth = (spriteIndex.w.value * divX) + cropX
  cropHeight = (spriteIndex.h.value * divY) + cropY

  cropBox = (cropX, cropY, cropWidth, cropHeight)
  croppedImage = images_list[currentImage].crop(cropBox)

  try:
    croppedImage.save("images/split/{}/{}.png".format(spriteIndex.location.value, spriteIndex.name.value))
  except:
    print("{} failed to export.".format(imageName))
    break