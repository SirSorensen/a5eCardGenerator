from Web_n_Data.Data_Interpreters.TableExtractor import TableExtractor
from Web_n_Data.Data_Interpreters.TableToDataStructure import TableToDataStructure
from Web_n_Data.File_Handlers import ObjectSaver
from Web_n_Data.Data_Structures.Spell import Spell

def scrape_spells_test(spell_page : int = 0):
    filepath = f"Outputs\Lists\Spells\source_text_{str(spell_page)}.txt"
    table_extractor = TableExtractor(filepath)
    table_to_data_structure = TableToDataStructure("Spell", save_object_to_file=True)
    list_of_spells = table_to_data_structure.make_data_structures(table_extractor)


def scrape_spells_test():
    abstraction_spell = Spell('Abstraction', scrape_source_text=False)
    if abstraction_spell is not None:
        print(abstraction_spell)
        abstraction_spell.prettify_soup()
        ObjectSaver.save_object(abstraction_spell)

    tiny_hut_spell = Spell('Tiny Hut', scrape_source_text=False)
    if tiny_hut_spell is not None:
        print(tiny_hut_spell)
        tiny_hut_spell.prettify_soup()
        ObjectSaver.save_object(tiny_hut_spell)

    fireball_spell = Spell('Fireball', scrape_source_text=False)
    if fireball_spell is not None:
        print(fireball_spell)
        fireball_spell.prettify_soup()
        ObjectSaver.save_object(fireball_spell)

def load_saved_spells_test():
    abstraction_spell = ObjectSaver.load_object('Abstraction', 'Spell')
    if abstraction_spell is not None:
        print(abstraction_spell)
        abstraction_spell.prettify_soup()
        ObjectSaver.save_object(abstraction_spell)

    tiny_hut_spell = ObjectSaver.load_object('Tiny Hut', 'Spell')
    if tiny_hut_spell is not None:
        print(tiny_hut_spell)
        tiny_hut_spell.prettify_soup()
        ObjectSaver.save_object(tiny_hut_spell)

    fireball_spell = ObjectSaver.load_object('Fireball', 'Spell')
    if fireball_spell is not None:
        print(fireball_spell)
        fireball_spell.prettify_soup()
        ObjectSaver.save_object(fireball_spell)
