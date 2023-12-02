# Importing Image class from PIL module
from PIL import Image
import os

sourceDir = r'Cards/DaggerFinal'

#  ---- Divider ----

#Number of files
totalFilesNumber = 0
for root_dir, cur_dir, files in os.walk(sourceDir):
    totalFilesNumber += len(files)

currentFileNumber = 0



#  ---- Painter ----

for dirpath, dirnames, filenames in os.walk(sourceDir):
    for filename in filenames:
        if filename.endswith('.png'):
            currentFileNumber += 1
            print(f"Painting {filename}, {currentFileNumber}/{totalFilesNumber}.")

            # Opens a image in RGB mode
            filepath = os.path.join(dirpath, filename)
            im = Image.open(filepath)
            
            # Size of the image in pixels (size of original image)
            # (This is not mandatory)
            width, height = im.size

            cardBorder = int((14/1591)*height)
            cornerBorder = int((30/1591)*height)

            #Colour upper-left corner
            for x in range(0,cornerBorder):
                yMax = cardBorder
                if x <= cardBorder:
                    yMax = cornerBorder
                
                for y in range(0,yMax):
                    im.putpixel( (x,y), (0,0,0))
            
            #Colour upper-right corner
            for x in range(width-cornerBorder,width):
                yMax = cardBorder
                if x >= width-cardBorder:
                    yMax = cornerBorder
                
                for y in range(0,yMax):
                    im.putpixel( (x,y), (0,0,0))
            
            #Colour lower-left corner
            for x in range(0,cornerBorder):
                yMin = height-cardBorder
                if x <= cardBorder:
                    yMin = height-cornerBorder
                
                for y in range(yMin, height):
                    im.putpixel( (x,y), (0,0,0))
            
            #Colour lower-right corner
            for x in range(width-cornerBorder,width):
                yMin = height-cardBorder
                if x >= width-cardBorder:
                    yMin = height-cornerBorder
                
                for y in range(yMin, height):
                    im.putpixel( (x,y), (0,0,0))

            # Saves the image in image viewer
            im.save(filepath)
            im.close()