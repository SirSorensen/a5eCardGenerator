from data_forge.data_structures.card import Card

field_classes = []

field_ids = []

class CombatManeuver(Card):
    def __init__(self, title : str, source_code : str, summary : str):
        # Title = "*"
        self.title = title
        # Summary = "*"
        self.summary = summary

        super(CombatManeuver, self).__init__(title, source_code, field_classes, field_ids)

        self.set_fields(self.extract_fields())
    
    def set_fields(self, field_dict : dict):
        return
        # Name = "*"
        self.name = field_dict.get('name')
        
        # Summary = "*"
        self.summary = field_dict.get('summary')

        # Description = "*"
        self.description = field_dict.get('description')

        # Points = 0, 1, 2, 3, 1-3
        self.points = field_dict.get('points')
        
        # Action Type = Action, Bonus Action, Bonus Action (Stance), Reaction, Other
        self.action_type = field_dict.get('action_type')

        # Degree: Basic manuever, 1st degree, 2nd degree, 3rd degree, 4th degree, 5th degree
        self.degree = field_dict.get('degree')

        # Tradition: None, Adamant Mountain, Arcane Knight, Beast Unity, Biting Zephyr, Eldritch Blackguard, Mirror’s Glint, Mist and Shade, Rapid Current, Razor’s Edge, Sanguine Knot, Spirited Steed, Tempered Iron, Tooth and Claw, Unending Wheel
        self.tradition = field_dict.get('tradition')

        # Prerequisite: "*"
        self.prerequisite = field_dict.get('prerequisite')

    