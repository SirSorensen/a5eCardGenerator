from data_forge.data_interpreters.card_interpreters.magic_item_interpreter import MagicItemInterpreter
from data_forge.data_structures.card import Card
from data_forge.data_structures.context_contents import Paragraphs
from data_forge.settings import *


class MagicItem(Card):
    def __init__(self, id : str, title : str, source_code : str):
        super(MagicItem, self).__init__(id, title, source_code)
    
    def set_fields(self, source_code : str):
        code_interpreter = MagicItemInterpreter(source_code)
        self.category = code_interpreter.get_category()
        self.rarity = code_interpreter.get_rarity()
        self.cost = code_interpreter.get_cost()
        self.crafting_components = code_interpreter.get_crafting_components()
        self.body = code_interpreter.get_body()
        self.source = code_interpreter.get_source()

    def set_text_fields(self):
        self.subtitle = f"{str(self.category)}, {str(self.rarity)}"
        self.icon = ""
        self.image = ""