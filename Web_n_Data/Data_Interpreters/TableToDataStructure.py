
import os
from Web_n_Data.Data_Interpreters.TableExtractor import TableExtractor
from Web_n_Data.Data_Structures.CardData import CardData
from Web_n_Data.Data_Structures.Spell import Spell
from Web_n_Data.File_Handlers.ObjectSaver import save_object, save_object_string


class TableToDataStructure:
    def __init__(self, type:str, save_object_to_file:bool = False):
        self.page = 0
        self.type = type.capitalize()
        self.save_to_file = save_object_to_file

    def make_data_structures(self, table_extractor : TableExtractor) -> list[CardData]:
        match self.type:
            case "Spell":
                return self.make_spell_data_structure(table_extractor)
            case "Feat":
                return self.make_feat_data_structure(table_extractor)
            case "CombatManeuver":
                return self.make_combat_manuever_data_structure(table_extractor)

    def make_spell_data_structure(self, table_extractor : TableExtractor) -> list[Spell]:
        list_of_names = table_extractor.extract_list_of_class_with_link("views-field views-field-title")
        list_of_all_summaries = table_extractor.extract_list_of_class("views-field views-field-field-spell-summary")

        list_of_spells : list[Spell] = []
        
        for i in range(len(list_of_names)):
            print(f"\nMaking spell data structure for {list_of_names[i][0]}...")
            os_filepath = r"Outputs\\Spells\\source_text_" + CardData.title_namer(list_of_names[i][0]) + r".txt"
            scrape_source_text=not os.path.exists(os_filepath)

            if scrape_source_text:
                print(f"{os_filepath} does not exist.")
            
            spell = Spell(
                name=list_of_names[i][0],
                web_url=list_of_names[i][1],
                summary=list_of_all_summaries[i],
                scrape_source_text=scrape_source_text
                )

            list_of_spells.append(spell)

            if self.save_to_file:
                save_object(spell)
                save_object_string(f"Outputs\\Spells\\Strings\\{spell.title}.txt", spell)
                print("\n")


        
        return list_of_spells

    def make_feat_data_structure(table_extractor : TableExtractor):
        pass

    def make_combat_manuever_data_structure(table_extractor : TableExtractor):
        pass


    
