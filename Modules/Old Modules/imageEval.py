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
            width, height = im.size

            x = (width/4)*3
            y = 1

            colour = im.getpixel((x, y))
            
            if colour == (0,0,0):
                print(f"File {filename} is good!")
            else:
                os.remove(filepath)

            im.close()