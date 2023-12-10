from enum import Enum

from data_forge.data_structures.context import Context

class Card:
    def __init__(self, context : Context
            ):
        
        self.context = context
        
        
        # self.title = title
        # self.subtitle = subtitle
        # self.description = description
        # self.image = Image(image_filepath)
        # self.icons = [Image(icon_filepath) for icon_filepath in icon_filepaths]
        # self.parts = parts
        # self.part = part
    


class Image:
    def __init__(self, filepath:str = ""):
        self.filepath = filepath

