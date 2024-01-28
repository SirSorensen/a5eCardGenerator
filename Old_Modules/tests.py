from Web_n_Data.Data_Interpreters.TableExtractor import TableExtractor
from Web_n_Data.Data_Interpreters.TableToDataStructure import TableToDataStructure
from Web_n_Data.Data_Structures.MagicItem import MagicItem
from Web_n_Data.File_Handlers.ObjectHandler import ObjectHandler
from Web_n_Data.Data_Structures.Spell import Spell
from Web_n_Data.Web_Scrapers.TableScraper import TableScraper

from Web_n_Data.Data_Structures.Tests.CardData_Tests import TestCardData







# Magic Item Tests
def extract_spells_from_magic_item_table_test(page : int = 0, save_object_to_file : bool = False, save_object_str_to_file:bool = False) -> list[Spell]:
    filepath = f"Outputs\Lists\MagicItems\source_text_"
    table_extractor = TableExtractor(filepath, page)
    table_to_data_structure = TableToDataStructure(MagicItem.__name__, 
                                                   save_object_to_file=save_object_to_file, 
                                                   save_object_str_to_file=save_object_str_to_file)
    return table_to_data_structure.make_data_structures(table_extractor)

def prettify_magic_items_test(list_of_spells: list[Spell]):
    for spell in list_of_spells:
        spell.get_pretty_code()

def scrape_magic_item_table_test():
    table_scraper = TableScraper(Spell.__name__)
    table_scraper.get_all_tables()



# Spell Tests
def extract_spells_from_spell_table_test(spell_page : int = 0, save_object_to_file : bool = False, save_object_str_to_file:bool = False) -> list[Spell]:
    filepath = f"Outputs\Lists\Spells\source_text_"
    table_extractor = TableExtractor(filepath, spell_page)
    table_to_data_structure = TableToDataStructure(Spell.__name__, save_object_to_file=save_object_to_file, save_object_str_to_file=save_object_str_to_file)
    return table_to_data_structure.make_data_structures(table_extractor)

def prettify_spells_test(list_of_spells: list[Spell]):
    for spell in list_of_spells:
        spell.get_pretty_code()

def scrape_spell_table_test():
    table_scraper = TableScraper(Spell.__name__)
    table_scraper.get_all_tables()

def scrape_spells_test():
    abstraction_spell = Spell('Abstraction', should_scrape_source_text=False)
    if abstraction_spell is not None:
        print(abstraction_spell)
        abstraction_spell.get_pretty_code()
        ObjectHandler.save_card_if_not_exists(abstraction_spell)

    tiny_hut_spell = Spell('Tiny Hut', should_scrape_source_text=False)
    if tiny_hut_spell is not None:
        print(tiny_hut_spell)
        tiny_hut_spell.get_pretty_code()
        ObjectHandler.save_card_if_not_exists(tiny_hut_spell)

    fireball_spell = Spell('Fireball', should_scrape_source_text=False)
    if fireball_spell is not None:
        print(fireball_spell)
        fireball_spell.get_pretty_code()
        ObjectHandler.save_card_if_not_exists(fireball_spell)

def load_saved_spells_test():
    abstraction_spell = ObjectHandler.load_object('Abstraction', 'Spell')
    if abstraction_spell is not None:
        print(abstraction_spell)
        abstraction_spell.get_pretty_code()
        ObjectHandler.save_card_if_not_exists(abstraction_spell)

    tiny_hut_spell = ObjectHandler.load_object('Tiny Hut', 'Spell')
    if tiny_hut_spell is not None:
        print(tiny_hut_spell)
        tiny_hut_spell.get_pretty_code()
        ObjectHandler.save_card_if_not_exists(tiny_hut_spell)

    fireball_spell = ObjectHandler.load_object('Fireball', 'Spell')
    if fireball_spell is not None:
        print(fireball_spell)
        fireball_spell.get_pretty_code()
        ObjectHandler.save_card_if_not_exists(fireball_spell)
