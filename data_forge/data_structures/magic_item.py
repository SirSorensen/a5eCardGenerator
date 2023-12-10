from data_forge.data_structures.card import Card


class MagicItem(Card):
    def __init__(self, name : str, url_ending : str = "", should_scrape_source_text : bool = False):
        print(f"Making a MagicItem! {name}, {url_ending}, {should_scrape_source_text}")

        super(MagicItem, self).__init__(name, url_ending, should_scrape_source_text)

        field_dict = self.extract_magic_item()

        # print("\n\n\n")
        # for key, value in field_dict.items():
        #     print(f"MagicItem field_dict key: {key}")
        #     if type(value) is list:
        #         for item in value:
        #             print(f"MagicItem field_dict item: {item}")
        #     else:
        #         print(f"MagicItem field_dict value: {value}")

        self.set_fields(field_dict)
    
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
        
    def scrape (self):
        return super(MagicItem, self).scrape()

    # This function extracts a spell from a source text
    def extract_magic_item(self):
        field_classes = [
            "field--name-field-mi-tags",
            "field--name-field-mi-crafting-components",
            "field--name-field-mi-description",
            "field--name-field-mi-source",
            "magic-item-category-rarity-cost"]

        field_ids = []

        field_dict = super(MagicItem, self).extract_fields(field_classes, field_ids)
        field_dict = super(MagicItem, self).extra_field_class("magic-item-category-rarity-cost", field_dict, True)

        return field_dict
        
    def __str__(self):
        # Create an empty list to store field name and value pairs
        field_strings = []

        # Iterate through all the attributes of the class
        for attr_name, attr_value in vars(self).items():
            # Exclude private attributes (those starting with underscores)
            if not attr_name.startswith('_'):
                if attr_value is list:
                    for item in attr_value:
                        field_strings.append(f"{attr_name}: {str(item)}")
                else:
                    field_strings.append(f"{attr_name}: {attr_value}")

        # Concatenate the field strings with newlines
        return '\n'.join(field_strings)

