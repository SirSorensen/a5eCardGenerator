from Web_n_Data.Data_Interpreters.DataStructureExtractor import DataStructureExtractor
from Web_n_Data.Web_Scrapers.a5eScraper import a5e_scrape_source_text


# This is meant as a superclass for CombatManuever, Feat, and Spell data structures.
class CardData:
    def __init__(self, name : str, url_ending : str, should_scrape_source_text : bool = False):
        self.data_name = CardData.name_to_data_name(name)

        if url_ending == "":
            print(f"ERROR! No web-url provided for {type(self).__name__.lower()} {name}!")    
        
        self.url_ending = url_ending

        if should_scrape_source_text: 
                self.scrape()
        
        self._code_interpreter = DataStructureExtractor(self.__get_filepath())

        
    # This function scrapes the source code of a card's data's internet page
    def scrape(self):        
        output_filepath = type(self).__name__ + r"s\\"

        return a5e_scrape_source_text(self.data_name, output_filepath, url_ending=self.url_ending)


    # This function reads the source text of a card's data from a file containing the source text of a card's data's internet page
    def __get_filepath(self) -> str:
        return r"Outputs\\" + type(self).__name__ + r"s\\source_text_" + self.data_name + r".html"
    
    # This function extracts a card's data from a source text
    def extract_fields(self, field_classes : list[str], field_ids : list[str]):
        field_dict = {}
        for class_ in field_classes:
            _code_interpreter : DataStructureExtractor= self._code_interpreter
            field_dict[CardData.key_namer(class_)] = _code_interpreter.extract_field_information(field_class=class_)
        
        for id in field_ids:
            _code_interpreter : DataStructureExtractor= self._code_interpreter
            field_dict[CardData.key_namer(id)] = _code_interpreter.extract_field_information(field_id=id)

        return field_dict

    def name_to_data_name(title : str):
        return title.replace(" ", "_").replace("/", "_").replace("’", "").replace("'", "").lower()

    def key_namer(key : str):
        return key.replace("field--", "").replace("name-", "").replace("field-", "").replace("spell-", "").replace("-indicator", "").replace("-", "_")
    
    def prettify_soup(self):
        self._code_interpreter.prettify_soup()