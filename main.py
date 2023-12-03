from Web_n_Data.Data_Interpreters.TableExtractor import TableExtractor
from Web_n_Data.Data_Interpreters.TableToDataStructure import TableToDataStructure
from Web_n_Data.File_Handlers.ObjectSaver import save_object, save_object_string


filepath = "Web_n_Data\Outputs\Lists\Spells\source_text_2.txt"
table_extractor = TableExtractor(filepath)
table_to_data_structure = TableToDataStructure("Spell")
list_of_spells = table_to_data_structure.make_data_structures(table_extractor)

for spell in list_of_spells:
    #print(spell)
    #print("\n\n\n")
    save_object(spell)
    save_object_string(f"Web_n_Data\\Outputs\\Spells\\Strings\\{spell.title}.txt", spell)