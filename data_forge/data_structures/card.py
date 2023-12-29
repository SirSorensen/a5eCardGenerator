import re
from data_forge.data_interpreters.code_interpreter import CodeInterpreter
from data_forge.settings import *
# This is meant as a superclass for CombatManuever, Feat, and Spell data structures.
class Card:
    def __init__(self, title : str, source_code : str, field_classes : list[str], field_ids : list[str]):

        self.title = title
        # data_name is the naming of the data structure when saved to a file.
        self.name = Card.to_context_name(title)

        if debug: print(f"Making a {type(self).__name__}! {self.name}")

        self._field_classes = field_classes
        self._field_ids = field_ids

        self._code_interpreter = CodeInterpreter(source_code)

        self.set_fields(self.extract_fields())

        # self.subtitle = subtitle
        # self.description = description
        # self.image = Image(image_filepath)
        # self.icons = [Image(icon_filepath) for icon_filepath in icon_filepaths]
        # self.parts = parts
        # self.part = part
        self.set_text_fields()

    def set_fields(self):
        raise NotImplementedError

    
    # This function extracts a card's data from a source text
    def extract_fields(self, field_dict : dict = {}) -> dict:
        if debug: print(f"Extracting fields from {self.name}...")
        for class_ in self._field_classes:
            field_info = self._code_interpreter.extract_field_information_from_class(class_)
            field_dict[self.key_namer(class_)] = field_info
        
        for id in self._field_ids:
            field_info = self._code_interpreter.extract_field_information_from_id(id)
            field_dict[self.key_namer(id)] = field_info

        return field_dict
            
    # This function converts an input string to a context name, by replacing spaces and special characters with underscores or nothing
    def to_context_name(input_str : str):
        context_name = input_str.lower()
        context_name = re.sub(r"[^\w\d]", "_", context_name)
        return context_name
    
    # This function sets the text fields of a card
    def set_text_fields(self):
        raise NotImplementedError
    
    def gen_description(self, body, split_str):
        description = str(body)
        paragraph_strs = description.split("\n")
        run_strs = []
        for paragraph_str in paragraph_strs:
            split_paragraph = paragraph_str.split(split_str)
            if len(split_paragraph) > 1:
                run_title = split_paragraph[0] + split_str
            else:
                run_title = ""
            run_body = paragraph_str[len(run_title):]
            run_strs.append((run_title, run_body))
        return run_strs

    # This function generates a key name from a field class or id
    def key_namer(self, key : str):
        key_name = key.lower()
        for ch in ["field--", "name-", "field-"]:
            key_name = key_name.replace(ch,"")
        
        key_name = Card.to_context_name(key_name)

        return key_name
    
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
                    field_strings.append(f"{attr_name}: {str(attr_value)}")

        # Concatenate the field strings with newlines
        return '\n\n'.join(field_strings)