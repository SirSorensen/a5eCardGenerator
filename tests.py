


from Web_n_Data.File_Handlers import PickleHandler
from Web_n_Data.Data_Structures import Spell


def scrape_spells_test():
    abstraction_spell = Spell('Abstraction', False)
    if abstraction_spell is not None:
        print(abstraction_spell)
        abstraction_spell.prettify_soup()
        PickleHandler.save_object(abstraction_spell)

    tiny_hut_spell = Spell('Tiny Hut', False)
    if tiny_hut_spell is not None:
        print(tiny_hut_spell)
        tiny_hut_spell.prettify_soup()
        PickleHandler.save_object(tiny_hut_spell)

    fireball_spell = Spell('Fireball', False)
    if fireball_spell is not None:
        print(fireball_spell)
        fireball_spell.prettify_soup()
        PickleHandler.save_object(fireball_spell)

def load_saved_spells_test():
    abstraction_spell = PickleHandler.load_object('Abstraction', 'Spell')
    if abstraction_spell is not None:
        print(abstraction_spell)
        abstraction_spell.prettify_soup()
        PickleHandler.save_object(abstraction_spell)

    tiny_hut_spell = PickleHandler.load_object('Tiny Hut', 'Spell')
    if tiny_hut_spell is not None:
        print(tiny_hut_spell)
        tiny_hut_spell.prettify_soup()
        PickleHandler.save_object(tiny_hut_spell)

    fireball_spell = PickleHandler.load_object('Fireball', 'Spell')
    if fireball_spell is not None:
        print(fireball_spell)
        fireball_spell.prettify_soup()
        PickleHandler.save_object(fireball_spell)
