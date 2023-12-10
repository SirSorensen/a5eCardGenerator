
import os

from data_forge.data_interpreters.table_interpreter import TableInterpreter

from data_forge.data_structures.card_data import CardData
from data_forge.data_structures.combat_maneuver import CombatManeuver
from data_forge.data_structures.magic_item import MagicItem
from data_forge.data_structures.spell import Spell
from data_forge.data_structures.feat import Feat

# This class extracts a list of data structures from a table
class TableToDataStructure:
    def __init__(self, card_type:str):
        self.page = 0
        self.card_type = card_type

    # This function extracts a list of data structures from a table
    def make_data_structures(self, table_extractor : TableInterpreter) -> list[CardData]:
        list_of_names = table_extractor.extract_list_of_names_with_link()
        if self.card_type == Spell.__name__:
            list_of_all_summaries = table_extractor.extract_list_of_summaries()

        card_data_list : list[CardData] = []
        
        for i in range(len(list_of_names)):
            print(f"Making a {self.card_type} data structure for {list_of_names[i][0]}...")
            os_filepath = f"Outputs\{self.card_type}s\source_text_" + CardData.name_to_data_name(list_of_names[i][0]) + r".html"

            should_scrape_source_text=not os.path.exists(os_filepath)
            if should_scrape_source_text:
                print(f"{os_filepath} does not exist.")
            
            if self.card_type == Spell.__name__:
                card_data = self.__make_card_data(list_of_names[i][0], list_of_names[i][1], should_scrape_source_text, list_of_all_summaries[i])
            else:
                card_data = self.__make_card_data(list_of_names[i][0], list_of_names[i][1], should_scrape_source_text)

            card_data_list.append(card_data)

        return card_data_list

    # This function makes a card data structure
    def __make_card_data(self, name : str, url_ending : str, should_scrape_source_text : bool, summary : str = "") -> Spell|Feat|CombatManeuver|CardData:       
        match self.card_type:
            case Spell.__name__:
                card_data = Spell(
                    name=name,
                    url_ending=url_ending,
                    summary=summary,
                    should_scrape_source_text=should_scrape_source_text
                )
            case Feat.__name__:
                card_data = Feat()
            case CombatManeuver.__name__:
                card_data = CombatManeuver()
            case MagicItem.__name__:
                card_data = MagicItem(
                    name=name,
                    url_ending=url_ending,
                    should_scrape_source_text=should_scrape_source_text
                    )
            case _:
                raise ValueError(f"ERROR! {self.card_type} is not a valid type!")

        return card_data
