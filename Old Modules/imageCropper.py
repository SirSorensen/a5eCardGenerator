# Importing Image class from PIL module
from PIL import Image
import os

directory = r'/Users/Daket12/Desktop/Cards'
for dirpath, dirnames, filenames in os.walk(directory):
    for filename in filenames:
        filepath = os.path.join(dirpath, filename)
        if filename.endswith('.zip'):
            os.remove(filepath)
        elif filename.endswith('.png'):
            # Opens a image in RGB mode
            im = Image.open(filepath)
            
            # Size of the image in pixels (size of original image)
            # (This is not mandatory)
            width, height = im.size

            # Setting the points for cropped image
            left = width * (375/2550)
            right = width * ((2550-376)/2550)
            top = height * (657/3300)
            bottom = height * ((3300-1144)/3300)
            
            # Cropped image of above dimension
            # (It will not change original image)
            im1 = im.crop((left, top, right, bottom))
            im.close()

            # Shows the image in image viewer
            #im1.show()
            im1.save(filepath)



