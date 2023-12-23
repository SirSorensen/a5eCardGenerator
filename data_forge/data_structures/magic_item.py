from data_forge.data_structures.card import Card
from data_forge.settings import *

field_classes = [
            "field--name-field-mi-tags",
            "field--name-field-mi-crafting-components",
            "field--name-field-mi-description",
            "field--name-field-mi-source",
            "magic-item-category-rarity-cost"]

field_ids = []

class MagicItem(Card):
    def __init__(self, title : str, source_code : str):
        super(MagicItem, self).__init__(title, source_code, field_classes, field_ids)
    
    def set_fields(self, field_dict : dict):
        # Tags = Attunement, Sentient, Charges, Consumable, Cursed
        tags = field_dict.get('tags')
        self.attunement = False
        self.component_seen = False
        self.charges = False
        self.consumable = False
        self.cursed = False
        if tags is not None:
            if type(tags) != list:
                tags = [tags]
            
            for tag in tags:
                match tag.lower().strip():
                    case "attunement":
                        self.attunement = True
                    case "sentient":
                        self.component_seen = True
                    case "charges":
                        self.charges = True
                    case "consumable":
                        self.consumable = True
                    case "cursed":
                        self.cursed = True
                    case _:
                        print(f"WARNING! Unrecognized tag {tag} for MagicItem {self.name}!")

        self.rarity = field_dict.get('rarity_cost')[0]
        self.price = field_dict.get('rarity_cost')[1]

        self.sub_title = field_dict.get('single-rarity-cost')

        self.body = field_dict.get('description')

        # Source = "*"
        self.source = field_dict.get('source')

    # This function generates a key name from a field class or id
    def key_namer(self, key : str):
        key_name = key.lower()
        for ch in ["mi-","magic-item-category-"]:
            key_name = key_name.replace(ch,"")
        
        key_name = super(MagicItem, self).key_namer(key_name)

        return key_name
    
    def set_text_fields(self):
        self.subtitle = str(self.sub_title)
        self.description = self.gen_description(self.body, ":")
        self.icon = ""
        self.image = ""
