# Importing Image class from PIL module
from PIL import Image
import os
import re

sourceDir = r'/Users/Daket12/Documents/Programmer(ing)/Private Projekter/CardimageCropper/Cards/Cropped Cards'
destinationDir = r'/Users/Daket12/Documents/Programmer(ing)/Private Projekter/CardimageCropper/Cards/Split Cards'

totalFilesNumber = 0
for root_dir, cur_dir, files in os.walk(sourceDir):
    totalFilesNumber += len(files)

currentFileNumber = 0

for dirpath, dirnames, filenames in os.walk(sourceDir):
    for filename in filenames:
        
        if filename.endswith('.png'):
            currentFileNumber += 1
            print(f"Dividing {filename}, {currentFileNumber}/{totalFilesNumber}.")

            # Opens a image in RGB mode
            filepath = os.path.join(dirpath, filename)
            im = Image.open(filepath)
            
            # Size of the image in pixels (size of original image)
            # (This is not mandatory)
            width, height = im.size

            # Setting the points for cropped image
            left = 0
            right = width
            middle = width/2
            top = 0
            bottom = height
            
            # Cropped image of above dimension
            # (It will not change original image)
            im1 = im.crop((left, top, middle, bottom))
            im2 = im.crop((middle, top, right, bottom))
            im.close()

            # Shows the image in image viewer
            #im1.show()
            filename1 = re.sub(r'Cards?_Print_', r'Front_', filename)
            filename2 = re.sub(r'Cards?_Print_', r'Back_', filename)
            im1.save(destinationDir + r'/Fronts/' + filename1)
            im2.save(destinationDir + r'/Backs/' + filename2)


#  ---- Painter ----

totalFilesNumber *= 2
currentFileNumber = 0
sourceDir = destinationDir

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

            cardBorder = int((16/1499)*height)
            cornerBorder = int((40/1499)*height)

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