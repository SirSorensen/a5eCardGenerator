

import bs4
from Web_n_Data.Data_Interpreters.CodeInterpreter import CodeInterpreter

# This class extracts data from the HTML of a data structure
class DataStructureExtractor(CodeInterpreter):
    def __init__(self, abs_filepath : str):
        super().__init__(abs_filepath)

    # This function extracts a field's information from a Tag object
    def __extract_field_information(self, field_div) -> list[str]|str:
        if field_div:
            item_fields = field_div.find_all('div', class_='field--item')
            if item_fields:
                return CodeInterpreter.prettify_list([CodeInterpreter.get_text(item) for item in item_fields])
                
            # Concatenate the text within <p> tags while preserving line breaks
            paragraphs = field_div.find_all('p')
            if paragraphs:
                return CodeInterpreter.prettify_list(['\n'.join(CodeInterpreter.get_text(p) for p in paragraphs)])
                
            spans = field_div.find_all('span')
            if spans:
                return CodeInterpreter.prettify_list([CodeInterpreter.get_text(s) for s in spans])

            return CodeInterpreter.prettify_list([CodeInterpreter.get_text(field_div)])
            
        return ""  # Field not found in the HTML
        
    # This function extracts a div-tag's tag object from an id
    def extract_field_information_from_id(self, field_id : str, flatten : bool = False) -> list[str]|str:
        field_div = self.soup.find('div', id=field_id)
        if not flatten:
            result = self.__extract_field_information(field_div)
        else:
            result = CodeInterpreter.get_text(field_div)

        if result == "":
            print(f"Id {field_id} not found in {self.abs_filepath}")
        return result

    # This function extracts a div-tag's tag object from a class
    def extract_field_information_from_class(self, field_class : str, flatten : bool = False) -> list[str]|str:
        field_div = self.soup.find('div', class_=field_class)
        if not flatten:
            result = self.__extract_field_information(field_div)
        elif field_div is not None:
            result = CodeInterpreter.prettify_list([CodeInterpreter.get_text(field_div)])
        else:
            result = ""

        if result == "":
            print(f"Id {field_class} not found in {self.abs_filepath}")
        return result



    # This function extracts the title of a card-data from the HTML
    def extract_name(self) -> str:
        name = self.soup.find('title')

        if name:
            return CodeInterpreter.get_text(name).replace("| Level Up", "").strip()
        return ""

