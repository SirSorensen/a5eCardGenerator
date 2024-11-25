from data_forge.data_interpreters.card_interpreters.spell_interpreter import SpellInterpreter
from data_forge.data_structures.card import Card
from data_forge.data_structures.context_contents import Paragraphs
from data_forge.settings import *

class Spell(Card):
    def __init__(self, id : str, title : str, source_code : str, summary : str):
        # Summary = "*"
        self.summary = summary
        super(Spell, self).__init__(id, title, source_code)

    
    def set_fields(self, source_code : str):
        code_interpreter = SpellInterpreter(source_code)
        self.level = code_interpreter.get_level()
        self.classical_school = code_interpreter.get_classical_school()
        self.schools = code_interpreter.get_schools()
        self.classes = code_interpreter.get_classes()
        self.casting_time = code_interpreter.get_casting_time()
        self.ritual = code_interpreter.get_ritual()
        self.range = code_interpreter.get_range()
        self.target = code_interpreter.get_target()
        self.area = code_interpreter.get_area()
        self.area_shape = code_interpreter.get_area_shape()
        self.component_material = code_interpreter.get_component_material()
        self.component_seen = code_interpreter.get_component_seen()
        self.component_vocalized = code_interpreter.get_component_vocalized()
        self.component_material_components = MaterialComponent(code_interpreter.get_component_material_components)
        self.duration = code_interpreter.get_duration()
        self.concentration = code_interpreter.get_concentration()
        self.saving_throw_desc = code_interpreter.get_saving_throw_desc()
        self.body = code_interpreter.get_body()
        self.spellcast_at_higher_levels = code_interpreter.get_spellcast_at_higher_levels()
        self.rare_versions = code_interpreter.get_rare_versions()
        self.source = code_interpreter.get_source()

    def set_text_fields(self):
        self.subtitle = f"Level {str(self.level)} {str(self.classical_school)} spell"
        self.icon = ""
        self.image = ""

class MaterialComponent:
    def __init__(self, code_interpreter_func):
        self.body, self.has_value, self.is_consumed = code_interpreter_func()

    def __str__(self):
        return str(self.body)
