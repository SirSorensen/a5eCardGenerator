
import os
from Web_n_Data.Data_Interpreters.TableExtractor import TableExtractor
from Web_n_Data.Data_Structures.CardData import CardData
from Web_n_Data.Data_Structures.CombatManeuver import CombatManeuver
from Web_n_Data.Data_Structures.Feat import Feat
from Web_n_Data.Data_Structures.Spell import Spell
from Web_n_Data.File_Handlers.ObjectSaver import ObjectSaver

# This class extracts a list of data structures from a table
class TableToDataStructure:
    def __init__(self, type_:str, save_object_to_file:bool = False, save_object_str_to_file:bool = False):
        self.page = 0
        self.type_ = type_.capitalize()
        self.save_object_to_file = save_object_to_file
        self.save_object_str_to_file = save_object_str_to_file

    # This function extracts a list of data structures from a table
    def make_data_structures(self, table_extractor : TableExtractor) -> list[CardData|Spell|Feat|CombatManeuver]:
        list_of_names = table_extractor.extract_list_of_names_with_link()
        list_of_all_summaries = table_extractor.extract_list_of_summaries()

        card_data_list : list[CardData|Spell|Feat|CombatManeuver] = []
        
        for i in range(len(list_of_names)):
            print(f"\nMaking a {self.type_} data structure for {list_of_names[i][0]}...")
            os_filepath = f"Outputs\{self.type_}s\source_text_" + CardData.name_to_data_name(list_of_names[i][0]) + r".html"
            

            should_scrape_source_text=not os.path.exists(os_filepath)
            if should_scrape_source_text:
                print(f"{os_filepath} does not exist.")
            
            card_data = self.__make_card_data(list_of_names[i][0], list_of_names[i][1], list_of_all_summaries[i], should_scrape_source_text)
        

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
    def __make_card_data(self, name : str, url_ending : str, summary : str, should_scrape_source_text : bool) -> Spell|Feat|CombatManeuver|CardData:
        if self.type_ == "Spell":
            card_data = Spell(
                name=name,
                url_ending=url_ending,
                summary=summary,
                should_scrape_source_text=should_scrape_source_text
                )
        elif self.type_ == "Feat":
            card_data = Feat(
                name=name,
                url_ending=url_ending,
                summary=summary,
                should_scrape_source_text=should_scrape_source_text
                )
        elif self.type_ == "CombatManeuver":
            card_data = CombatManeuver(
                name=name,
                url_ending=url_ending,
                summary=summary,
                should_scrape_source_text=should_scrape_source_text
                )
        else:
            raise ValueError(f"ERROR! {self.type_} is not a valid type!")

        return card_data
