from enum import Enum

class Card:
    def __init__(self,
            title          : str       = ""  , subtitle       : str = "",
            description    : str       = ""  , image_filepath : str = "",
            icon_filepaths : list[str] = [""], type           : str = "",
            parts          : int       = 1   , part           : int = 1
            ):
        self.title = title
        self.subtitle = subtitle
        self.description = description
        self.image = Image(image_filepath)
        self.icons = [Image(icon_filepath) for icon_filepath in icon_filepaths]
        self.type = CardType[type.toUpperCase()]
        self.parts = parts
        self.part = part
    


class Image:
    def __init__(self, filepath:str = ""):
        self.filepath = filepath

class CardType(Enum):
    SPELL = 1
    COMBAT_MANEUVER = 2
    FEAT = 3
    MAGIC_ITEM = 4
