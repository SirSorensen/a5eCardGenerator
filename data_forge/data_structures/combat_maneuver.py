from data_forge.data_structures.card import Card
from data_forge.settings import *


field_classes = [
    'combat-maneuver-points-actions',
    'combat-maneuver-degree-tradition-action-type',
    'field--name-body',
    'combat-maneuver-prerequisite',
    'combat-maneuver-source'
]

field_ids = []

class CombatManeuver(Card):
    def __init__(self, title : str, source_code : str, summary : str):
        # Summary = "*"
        self.summary = summary

        super(CombatManeuver, self).__init__(title, source_code, field_classes, field_ids)

        self.set_fields(self.extract_fields())
    
    def set_fields(self, field_dict : dict):        
        # Description = "*"
        self.description = field_dict.get('name_body')

        # Points = 0, 1, 2, 3, 1-3
        self.points = field_dict.get('points_actions')
        
        self.degree_tradition_action_type = field_dict.get('degree_tradition_action_type')
        # Action Type = Action, Bonus Action, Bonus Action (Stance), Reaction, Other
        # self.action_type = field_dict.get('action_type')

        # Degree: Basic manuever, 1st degree, 2nd degree, 3rd degree, 4th degree, 5th degree
        # self.degree = field_dict.get('degree')

        # Tradition: None, Adamant Mountain, Arcane Knight, Beast Unity, Biting Zephyr, Eldritch Blackguard, Mirror’s Glint, Mist and Shade, Rapid Current, Razor’s Edge, Sanguine Knot, Spirited Steed, Tempered Iron, Tooth and Claw, Unending Wheel
        # self.tradition = field_dict.get('tradition')

        # Prerequisite: "*"
        self.prerequisite = field_dict.get('prerequisite')
    
    # This function generates a key name from a field class or id
    def key_namer(self, key : str):
        key_name = key.lower()
        for ch in ["combat-maneuver-"]:
            key_name = key_name.replace(ch,"")
        
        key_name = super(CombatManeuver, self).key_namer(key_name)

        return key_name

    