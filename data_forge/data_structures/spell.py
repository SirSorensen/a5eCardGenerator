from data_forge.data_structures.card import Card
from data_forge.settings import *

field_classes = [
            "field--name-field-spell-level",
            "field--name-field-classical-spell-school",
            "field--name-field-spell-schools",
            "field--name-field-spell-classes",
            "field--name-field-spell-casting-time",
            "field--name-field-spell-range",
            "field--name-field-area-shape",
            "field--name-field-spell-target",
            "field--name-field-spell-area",
            "field--name-field-spellcomponent-description",
            "field--name-field-spell-saving-throw-desc",
            "field--name-field-spellcast-at-higher-levels",
            "field--name-field-spell-source",
            "field--name-body",
            "field--name-field-spell-rare-versions",
            "ritual-indicator"]

field_ids = [
    "spell-components-display",
    "duration",
    "spell-summary"
    ]

class Spell(Card):
    def __init__(self, title : str, source_code : str, summary : str):
        # Summary = "*"
        self.summary = summary
        super(Spell, self).__init__(title, source_code, field_classes, field_ids)

    
    def set_fields(self, field_dict : dict):
        # Level = Cantrip/0, 1st, 2nd, 3rd, 4th, 5th, 6th, 7th, 8th, 9th
        self.level = field_dict.get('level')
        # Classical School = Abjuration, Conjuration, Divination, Enchantment, Evocation, Illusion, Necromancy, Transmutation
        self.classical_school = field_dict.get('classical_school')
        # Spell School(s) = Acid, Affliction, Air, Arcane, Attack, Beasts, Chaos, Cold, Communication, Compulsion, Divine, Earth, Enhancement, Evil, Fear, Fire, Force, Good, Healing, Knowledge, Law, Lightning, Movement, Nature, Necrotic, Negation, Obscurement, Planar, Plants, Poison, Prismatic, Protection, Psychic, Radiant, Scrying, Senses, Shadow, Shapechanging, Sound, Storm, Summoning, Technological, Teleportation, Terrain, Thunder, Transformation, Utility, Water, Weaponry, Weather
        self.schools = field_dict.get('schools')
        # Class(es) = Artificer, Bard, Cleric, Druid, Herald, Sorcerer, Warlock, Wizard
        self.classes = field_dict.get('classes')
        # Casting Time = 1 Action, 1 Bonus Action, 1 Hour, 1 Minute, 1 Reaction, 10 Minutes, 12 Hours, 24 Hours, 8 Hours, 1 Week
        self.casting_time = field_dict.get('casting_time')
        # Ritual? = True, False
        self.ritual = field_dict.get('ritual') == "r"
        # Range = Self, Touch, Short (30 feet), Medium (60 feet), Long (120 feet),Unlimited, Special
        self.range = field_dict.get('range')
        # Target = "*"
        self.target = field_dict.get('target')
        # Area = "*" (often "<x> feet (radius <area-shape>)?")
        self.area = field_dict.get('area')
        # Area Shape = Cone, Cube, Cylinder, Line, Sphere
        self.area_shape = field_dict.get('area_shape')
        # Components = Material, Seen, Vocalized
        # Material Components = "*"
        self.component_material = False
        self.component_seen = False
        self.component_vocalized = False
        self.component_material_components = None
        
        if field_dict.get('components_display') is not None:
            for component in field_dict.get('components_display'):
                if component.lower().startswith("material"):
                    self.component_material = True
                    self.component_material_components = [MaterialComponent(text) for text in field_dict.get('spellcomponent_description').split(",")]
                elif component.lower().startswith("seen"):
                    self.component_seen = True
                elif component.lower().startswith("vocalized"):
                    self.component_vocalized = True

        # Duration = Instantaneous, 1 round, 1 minute, 10 minutes, 1 hour, 8 hours, 24 hours, 7 days, 10 days, 30 days, Until dispelled, Until dispelled or triggered, Special, Concentration (1 round), Concentration (1 minute), Concentration (10 minutes), Concentration (1 hour), Concentration (8 hours), Concentration (24 hours), Concentration (7 days), Concentration (10 days), Concentration (30 days), Concentration (Until dispelled), Concentration (Until dispelled or triggered), Concentration (Special)
        self.duration = field_dict.get('duration')
        # Saving Throw = "*"
        self.saving_throw_desc = field_dict.get('saving_throw_desc')
        # Description = "*"
        self.body = field_dict.get('body')
        # Cast at Higher Levels = "*"
        self.spellcast_at_higher_levels = field_dict.get('spellcast_at_higher_levels')
        # Rare versions = (title:"*", description:"*")
        self.rare_versions = field_dict.get('rare_versions')
        # Source = "*"
        self.source = field_dict.get('source')
    
    # This function generates a key name from a field class or id
    def key_namer(self, key : str):
        key_name = key.lower()
        for ch in ["spell-", "-indicator"]:
            key_name = key_name.replace(ch,"")
        
        key_name = super(Spell, self).key_namer(key_name)

        return key_name


    def set_text_fields(self):
        self.subtitle = str(self.classes)
        self.description = self.gen_description(self.body, ":")
        self.icon = ""
        self.image = ""


class MaterialComponent:
    def __init__(self, text: str):
        self.text = text
        self.consumed = MaterialComponent.evalIfConsumed(text)
        
    # TODO: Check if this works
    def evalIfConsumed(text: str) -> bool:
        return "consumed" in text.lower()

    def __str__(self):
        return f"Consumed? {self.consumed}\n{self.text}"
