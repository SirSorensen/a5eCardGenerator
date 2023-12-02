from Web.SourceCodeInterpreter import CodeInterpreter
from Web.a5eScraper import a5e_scrape_source_text


# This is meant as a superclass for CombatManuever, Feat, and Spell data structures.
class CardData:  
    # This function scrapes the source code of a card's data's internet page
    def scrape (self, name : str):
        
        print(f"Scraping {type(self).__name__}: {name}...")
        
        output_filepath = r"Outputs\\" + type(self).__name__ + r"s\\"

        return a5e_scrape_source_text(name, "spell/", output_filepath)


    # This function reads the source text of a card's data from a file containing the source text of a card's data's internet page
    def get_filepath(self, filename : str) -> str:
        return r"Outputs\\" + type(self).__name__ + r"s\\source_text_" + filename + r".txt"
    
    # This function extracts a card's data from a source text
    def extract_fields(self, field_classes : list[str], field_ids : list[str]):
        print(f"Extracting {type(self).__name__}...")

        field_dict = {}
        for class_ in field_classes:
            _code_interpreter : CodeInterpreter= self._code_interpreter
            field_dict[CardData.key_namer(class_)] = _code_interpreter.extract_field_information(field_class=class_)
        
        for id in field_ids:
            _code_interpreter : CodeInterpreter= self._code_interpreter
            field_dict[CardData.key_namer(id)] = _code_interpreter.extract_field_information(field_id=id)

        return field_dict

    def key_namer(key : str):
        return key.replace("field--", "").replace("name-", "").replace("field-", "").replace("spell-", "").replace("-indicator", "").replace("-", "_")
    
    def prettify_soup(self):
        self._code_interpreter.prettify_soup()