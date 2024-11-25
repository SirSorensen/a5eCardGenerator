import json
import re
from data_forge.settings import *
# This is meant as a superclass for CombatManuever, Feat, and Spell data structures.
class Card:
    def __init__(self, id : str, title : str, source_code : str):

        self.title = title
        # data_name is the naming of the data structure when saved to a file.
        self.name = Card.to_context_name(title)
        self.type = type(self).__name__

        if debug: print(f"Making a {type(self).__name__}! {self.name}")
        
        # Set the fields of the class
        self.set_fields(source_code)
        self.set_text_fields()

    def set_fields(self):
        raise NotImplementedError
            
    # This function converts an input string to a context name, by replacing spaces and special characters with underscores or nothing
    def to_context_name(input_str : str):
        context_name = input_str.lower()
        context_name = re.sub(r"[^\w\d]", "_", context_name)
        return context_name
    
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
    
