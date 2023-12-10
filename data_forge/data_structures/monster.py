from data_forge.data_structures.card import Card

field_classes = []

field_ids = []

class Monster(Card):
    def __init__(self, title : str, source_code : str):
        # Title = "*"
        self.title = title

        super(Monster, self).__init__(title, source_code, field_classes, field_ids)

        self.set_fields(self.extract_fields())
    
    def set_fields(self, field_dict : dict):
        pass

