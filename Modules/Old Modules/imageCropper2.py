# Importing Image class from PIL module
from PIL import Image
import os

directory = r'Cards/Dagger'
for dirpath, dirnames, filenames in os.walk(directory):
    for filename in filenames:
        filepath = os.path.join(dirpath, filename)
        if filename.endswith('.zip'):
            os.remove(filepath)
        elif filename.endswith('.png'):
            print("Found " + filename)
            # Opens a image in RGB mode
            im = Image.open(filepath)
            
            # Size of the image in pixels (size of original image)
            # (This is not mandatory)
            width, height = im.size

            # Setting the points for cropped image
            left = width * (236/2339)
            right = width * ((2339-239)/2339)
            top = height * (30/1654)
            bottom = height * ((1654-33)/1654)
            
            # Cropped image of above dimension
            # (It will not change original image)
            im1 = im.crop((left, top, right, bottom))
            im.close()

            # Shows the image in image viewer
            #im1.show()
            im1.save(filepath)



