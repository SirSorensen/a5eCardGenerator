
import unittest
from data_forge.controller import Controller
from data_forge.data_interpreters.table_interpreter import TableInterpreter
from data_forge.table_to_data_structure import TableToDataStructure
from data_forge.data_structures.spell import Spell
from data_forge.file_handlers.object_handler import ObjectHandler


class SpellTests(unittest.TestCase):
    def extract_spells_from_spell_table_test(spell_page : int = 0, save_object_to_file : bool = False, save_object_str_to_file:bool = False) -> list[Spell]:
        filepath = f"Outputs\Lists\Spells\source_text_"
        table_extractor = TableInterpreter(filepath, spell_page)
        table_to_data_structure = TableToDataStructure(Spell.__name__, save_object_to_file=save_object_to_file, save_object_str_to_file=save_object_str_to_file)
        return table_to_data_structure.make_data_structures(table_extractor)

    def prettify_spells_test(list_of_spells: list[Spell]):
        for spell in list_of_spells:
            spell.prettify_html()

    def scrape_spell_table_test():
        table_scraper = Controller(Spell.__name__)
        table_scraper.get_all_tables()

    def scrape_spells_test():
        abstraction_spell = Spell('Abstraction')
        if abstraction_spell is not None:
            print(abstraction_spell)

        tiny_hut_spell = Spell('Tiny Hut')
        if tiny_hut_spell is not None:
            print(tiny_hut_spell)

        fireball_spell = Spell('Fireball')
        if fireball_spell is not None:
            print(fireball_spell)

    def load_saved_spells_test():
        abstraction_spell = ObjectHandler.load_object('Abstraction', 'Spell')
        if abstraction_spell is not None:
            print(abstraction_spell)

        tiny_hut_spell = ObjectHandler.load_object('Tiny Hut', 'Spell')
        if tiny_hut_spell is not None:
            print(tiny_hut_spell)

        fireball_spell = ObjectHandler.load_object('Fireball', 'Spell')
        if fireball_spell is not None:
            print(fireball_spell)