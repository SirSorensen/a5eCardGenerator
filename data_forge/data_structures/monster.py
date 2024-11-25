from data_forge.data_interpreters.card_interpreters.monster_interpreter import MonsterInterpreter
from data_forge.data_structures.card import Card
from data_forge.settings import *

class Monster(Card):
    def __init__(self, id : str, title : str, source_code : str):
        super(Monster, self).__init__(id, title, source_code)
    
    def set_fields(self, source_code : str):
        code_interpreter = MonsterInterpreter(source_code)
        self.size = code_interpreter.get_size()
        self.monster_type = code_interpreter.get_type()
        self.challenge_rating = code_interpreter.get_challenge_rating()
        self.terrain = code_interpreter.get_terrain()
        self.strength_val = code_interpreter.get_strength_val()
        self.dexterity_val = code_interpreter.get_dexterity_val()
        self.constitution_val = code_interpreter.get_constitution_val()
        self.intelligence_val = code_interpreter.get_intelligence_val()
        self.wisdom_val = code_interpreter.get_wisdom_val()
        self.charisma_val = code_interpreter.get_charisma_val()
        self.body = code_interpreter.get_stat_block()
        self.monster_description = code_interpreter.get_description()
        self.behavior = code_interpreter.get_behavior()
        self.encounters = code_interpreter.get_encounters()
        self.type_description = code_interpreter.get_type_description()
        self.source = code_interpreter.get_source()

    def set_text_fields(self):
        self.subtitle = f"{str(self.size)} {str(self.type)}"
        self.icon = ""
        self.image = ""
