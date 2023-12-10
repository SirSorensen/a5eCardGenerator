from data_forge.data_structures.card import Card

field_classes = [
            "field--name-field-mi-tags",
            "field--name-field-mi-crafting-components",
            "field--name-field-mi-description",
            "field--name-field-mi-source",
            "magic-item-category-rarity-cost"]

field_ids = []

class MagicItem(Card):
    def __init__(self, title : str, source_code : str):
        # Title = "*"
        self.title = title

        super(MagicItem, self).__init__(title, source_code, field_classes, field_ids)

        self.set_fields(self.extract_fields())
    
    def set_fields(self, field_dict : dict):
        # Name = "*"
        self.name = self._code_interpreter.extract_name()

        if field_dict.get('tags') is not None:
            for tag in field_dict.get('tags'):
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

    # This function extracts a spell from a source text
    def extract_fields(self):
        field_dict = super(MagicItem, self).extract_fields()
        field_dict = super(MagicItem, self).extra_field_class("magic-item-category-rarity-cost", field_dict, True)
        return field_dict

