from Web.SourceCodeInterpreter import CodeInterpreter
from Web.a5eScraper import a5e_scrape_source_text


# This is meant as a superclass for CombatManuever, Feat, and Spell data structures.
class CardData:  
    # This function scrapes the source code of a card's data's internet page
    def scrape (self, name : str):
        name = name.replace(" ", "-").lower()
        print(f"Scraping {type(self).__name__}: {name}...")
        
        output_filepath = r"Outputs\\" + type(self).__name__ + r"s\\"
        
        return a5e_scrape_source_text(name, "spell/", output_filepath)


    # This function reads the source text of a card's data from a file containing the source text of a card's data's internet page
    def read_file(self, name : str) -> str:
        file_name = name.replace(" ", "-").lower()

        filepath = r"Outputs\\" + type(self).__name__ + r"s\\source_text_" + file_name + r".txt"

        with open(filepath, "r", encoding='utf-8') as file:
            return file.read()
    
    # This function extracts a card's data from a source text
    def extract_fields(self, field_classes : list[str], field_ids : list[str]):
        print(f"Extracting {type(self).__name__}...")

        field_dict = {}
        for class_ in field_classes:
            code_interpreter : CodeInterpreter= self.code_interpreter
            field_dict[class_] = code_interpreter.extract_field_information(field_class=class_)
        
        for id in field_ids:
            code_interpreter : CodeInterpreter= self.code_interpreter
            field_dict[id] = code_interpreter.extract_field_information(field_id=id)
    
        return field_dict