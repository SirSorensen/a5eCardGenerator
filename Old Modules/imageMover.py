# Importing Image class from PIL module
from PIL import Image
import os

directory = r'/Users/Daket12/Desktop/Cards'
for dirpath, dirnames, filenames in os.walk(directory):
    for filename in filenames:
        filepath = os.path.join(dirpath, filename)
        if filename.endswith('.png'):
            os.rename(filepath, r'/Users/Daket12/Desktop/Cards/' + filename)