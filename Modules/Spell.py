
class Spell:
    def __init__(self):
        self.name = ""
        self.summary = ""
        self.level = 0
        self.classical_school = ""
        self.spell_schools = [""]
        self.classes = [""]
        self.casting_time = ""
        self.ritual = False
        self.range = ""
        self.target = ""
        self.area = ""
        self.area_shape = ""
        self.component_material = (False, "")
        self.component_seen = False
        self.component_vocalized = False
        self.duration = ""
        self.saving_throw = ""

        self.description = ""

        self.cast_at_higher_levels = ""

        self.rare_vesions = [("","")]

        self.source = ""

class MaterialComponent:
    def __init__(self, text: str):
        self.text = text
        self.consumed = False
    
    #TODO
    def evalIfConsumed(text: str) -> bool:
        if s