from Web_n_Data.Data_Interpreters.DataStructureExtractor import DataStructureExtractor
from Web_n_Data.Web_Scrapers.a5eScraper import a5e_scrape_source_text


# This is meant as a superclass for CombatManuever, Feat, and Spell data structures.
class CardData:
    def __init__(self, web_location : str, web_url : str = "", scrape_source_text : bool = False):
        self.title = web_location

        if web_url == "":
            self.web_url = web_location
        else:
            self.web_url = web_url

        if scrape_source_text: 
                self.scrape(web_url)
        
        self._code_interpreter = DataStructureExtractor(self.get_filepath(web_location))

        
    # This function scrapes the source code of a card's data's internet page
    def scrape(self):        
        output_filepath = type(self).__name__ + r"s\\"

        return a5e_scrape_source_text(self.title, "", output_filepath, web_url=self.web_url)


    # This function reads the source text of a card's data from a file containing the source text of a card's data's internet page
    def get_filepath(self, filename : str) -> str:
        return r"Web_n_Data\\Outputs\\" + type(self).__name__ + r"s\\source_text_" + filename + r".txt"
    
    # This function extracts a card's data from a source text
    def extract_fields(self, field_classes : list[str], field_ids : list[str]):
        print(f"Extracting fields for {type(self).__name__} \'{self.title}\'...")

        field_dict = {}
        for class_ in field_classes:
            _code_interpreter : DataStructureExtractor= self._code_interpreter
            field_dict[CardData.key_namer(class_)] = _code_interpreter.extract_field_information(field_class=class_)
        
        for id in field_ids:
            _code_interpreter : DataStructureExtractor= self._code_interpreter
            field_dict[CardData.key_namer(id)] = _code_interpreter.extract_field_information(field_id=id)

        return field_dict

    

    def key_namer(key : str):
        return key.replace("field--", "").replace("name-", "").replace("field-", "").replace("spell-", "").replace("-indicator", "").replace("-", "_")
    
    def prettify_soup(self):
        self._code_interpreter.prettify_soup()