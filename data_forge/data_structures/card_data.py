import re


# This is meant as a superclass for CombatManuever, Feat, and Spell data structures.
class CardData:
    def __init__(self, name : str, url_ending : str, should_scrape_source_text : bool = False):
        # data_name is the naming of the data structure when saved to a file.
        self.data_name = CardData.name_to_data_name(name)

        # url_ending is the ending of the web-url of the card's data's internet page.
        self.url_ending = url_ending
        if url_ending == "":
            print(f"ERROR! No web-url provided for {type(self).__name__.lower()} {name}!")    

    # This function reads the source text of a card's data from a file containing the source text of a card's data's internet page
    def __get_filepath(self) -> str:
        return r"Outputs\\" + type(self).__name__ + r"s\\source_text_" + self.data_name + r".html"
    
    # This function extracts a card's data from a source text
    def extract_fields(self, field_classes : list[str], field_ids : list[str], field_dict : dict = {},  flatten : bool = False) -> dict:
        print(f"Extracting fields from {self.data_name}...")
        for class_ in field_classes:
            field_info = self._code_interpreter.extract_field_information_from_class(class_, flatten=flatten)
            field_dict[CardData.key_namer(class_)] = field_info
        
        for id in field_ids:
            field_info = self._code_interpreter.extract_field_information_from_id(id, flatten=flatten)
            field_dict[CardData.key_namer(id)] = field_info

        return field_dict

    def extra_field_class(self, field_class : str, field_dict : dict = {},  flatten : bool = False):
            field_info = self._code_interpreter.extract_field_information_from_class(field_class, flatten=flatten)
            field_dict[CardData.key_namer(f"single-{field_class}")] = field_info
            return field_dict
            
    # This function converts a card's name to a data name, by replacing spaces and special characters with underscores or nothing
    def name_to_data_name(name : str):
        data_name = name.lower()
        data_name = re.sub(r"[^\w\d]", "_", data_name)
        return data_name

    # This function generates a key name from a field class or id
    def key_namer(key : str):
        key_name = key.lower()
        for ch in ["field--", "name-", "field-", "spell-", "mi-", "magic-item-", "category-", "-indicator"]:
            key_name = key_name.replace(ch,"")
        
        key_name = CardData.name_to_data_name(key_name)

        return key_name