from Web_n_Data.Data_Interpreters.TableExtractor import TableExtractor
from Web_n_Data.Data_Interpreters.TableToDataStructure import TableToDataStructure


filepath = "Web_n_Data\Outputs\Lists\Spells\source_text_3.txt"
table_extractor = TableExtractor(filepath)
table_to_data_structure = TableToDataStructure("Spell")
list_of_spells = table_to_data_structure.make_data_structures(table_extractor)

for spell in list_of_spells:
    print(spell)
    print("\n\n\n")