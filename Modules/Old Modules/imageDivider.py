# Importing Image class from PIL module
from PIL import Image
import os
import re

sourceDir = r'Cards/Dagger'
destinationDir = r'Cards/DaggerFinal'

for dirpath, dirnames, filenames in os.walk(sourceDir):
    for filename in filenames:
        
        if filename.endswith('.png'):
            print(f"Dividing {filename}")

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