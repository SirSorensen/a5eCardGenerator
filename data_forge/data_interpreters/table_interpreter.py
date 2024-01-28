from data_forge.settings import *
from data_forge.data_interpreters.code_interpreter import CodeInterpreter
from data_forge.data_structures.spell import Spell
from data_forge.data_structures.combat_maneuver import CombatManeuver

name_tag_class = "views-field-title"
summary_spell_tag_class = "views-field-field-spell-summary"
summary_combatManuever_tag_class = "views-field-field-cm-summary"

summary_tag_class_dict = {
  Spell.__name__: "views-field-field-spell-summary",
  CombatManeuver.__name__: "views-field-field-cm-summary"
}

# This class extracts data from the HTML of a table
class TableInterpreter(CodeInterpreter):
    def __init__(self, source_code : str):
        super().__init__(source_code, 'table')

    # This function extracts a the contents of list tags from a source text 
    def __extract_list_of_class(self, class_:str) -> list[str]|str:
        field_td = self.soup.find_all('td', class_=class_)
        return CodeInterpreter.prettify_list(field_td)

    # This function extracts a the contents of list tags and their hyper-links from a source text
    def __extract_list_of_class_with_link(self, class_:str):
        field_td = self.soup.find_all('td', class_=class_)

        results = [(CodeInterpreter.get_text(item), item.find('a')['href']) for item in field_td]
            
        return results    
        # return CodeInterpreter.prettify_list(results)


    # This function extracts the names their hyper-links of a table
    def extract_list_of_names_with_link(self):
        return self.__extract_list_of_class_with_link(name_tag_class)


    # This function extracts the summaries of a table
    # TODO: Right now it goes through summaries of combat manuever and spells. It should only go through one or the other, or a third given option.
    def extract_list_of_summaries(self, card_type) -> list[str]|str:
        summary_tag = summary_tag_class_dict.get(card_type)
        if summary_tag is None:
            if debug: print("ERROR: Card type does not have a summary tag!")
            return []
        
        list_of_summaries = self.__extract_list_of_class(summary_tag)

        if len(list_of_summaries) == 0:
            if debug: print("ERROR: No summaries found!")
        
        return list_of_summaries


    # This function evaluates whether or not there is a next page
    def is_next_page(self) -> bool:
        next_page_li = self.soup.find('li', class_="next")
        return next_page_li is not None
    