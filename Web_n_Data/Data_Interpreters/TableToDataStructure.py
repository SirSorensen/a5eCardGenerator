
import os
from Web_n_Data.Data_Interpreters.TableExtractor import TableExtractor
from Web_n_Data.Data_Structures.CardData import CardData
from Web_n_Data.Data_Structures.CombatManeuver import CombatManeuver
from Web_n_Data.Data_Structures.Feat import Feat
from Web_n_Data.Data_Structures.MagicItem import MagicItem
from Web_n_Data.Data_Structures.Spell import Spell
from Web_n_Data.File_Handlers.ObjectSaver import ObjectSaver

# This class extracts a list of data structures from a table
class TableToDataStructure:
    def __init__(self, card_data_type:str, save_object_to_file:bool = False, save_object_str_to_file:bool = False):
        self.page = 0
        self.card_data_type = card_data_type
        self.save_object_to_file = save_object_to_file
        self.save_object_str_to_file = save_object_str_to_file

    # This function extracts a list of data structures from a table
    def make_data_structures(self, table_extractor : TableExtractor) -> list[CardData]:
        list_of_names = table_extractor.extract_list_of_names_with_link()
        if self.card_data_type == Spell.__name__:
            list_of_all_summaries = table_extractor.extract_list_of_summaries()

        card_data_list : list[CardData] = []
        
        for i in range(len(list_of_names)):
            print(f"\nMaking a {self.card_data_type} data structure for {list_of_names[i][0]}...")
            os_filepath = f"Outputs\{self.card_data_type}s\source_text_" + CardData.name_to_data_name(list_of_names[i][0]) + r".html"

            should_scrape_source_text=not os.path.exists(os_filepath)
            if should_scrape_source_text:
                print(f"{os_filepath} does not exist.")
            
            if self.card_data_type == Spell.__name__:
                card_data = self.__make_card_data(list_of_names[i][0], list_of_names[i][1], should_scrape_source_text, list_of_all_summaries[i])
            else:
                card_data = self.__make_card_data(list_of_names[i][0], list_of_names[i][1], should_scrape_source_text)

            card_data_list.append(card_data)

            if self.save_object_to_file:
                print(f"Pickling {type(card_data).__name__} \'{card_data.name}\' to file...")
                ObjectSaver.save_object(card_data)
            if self.save_object_str_to_file:
                print(f"Saving string of {type(card_data).__name__} \'{card_data.name}\' to file...")
                ObjectSaver.save_object_string(card_data)
            print("\n")

        return card_data_list

    # This function makes a card data structure
    def __make_card_data(self, name : str, url_ending : str, should_scrape_source_text : bool, summary : str = "") -> Spell|Feat|CombatManeuver|CardData:       
        match self.card_data_type:
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
                raise ValueError(f"ERROR! {self.card_data_type} is not a valid type!")

        return card_data
