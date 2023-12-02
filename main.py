from FileHandler.PickleHandler import save_object, load_object
from Data_Structures.Spell import Spell

#spell_source_text = scrape_spell("Abstraction")
#print("Encoding = " + spell_source_text.encoding)

abstraction_spell = Spell('Abstraction', False)
if abstraction_spell is not None:
    print(abstraction_spell)
    abstraction_spell.prettify_soup()
    save_object(abstraction_spell)

tiny_hut_spell = Spell('Tiny Hut', False)
if tiny_hut_spell is not None:
    print(tiny_hut_spell)
    tiny_hut_spell.prettify_soup()
    save_object(tiny_hut_spell)

fireball_spell = Spell('Fireball', False)
if fireball_spell is not None:
    print(fireball_spell)
    fireball_spell.prettify_soup()
    save_object(fireball_spell)


# abstraction_spell = load_object('Abstraction', 'Spell')
# if abstraction_spell is not None:
#     print(abstraction_spell)
#     abstraction_spell.prettify_soup()
#     save_object(abstraction_spell)

# tiny_hut_spell = load_object('Tiny Hut', 'Spell')
# if tiny_hut_spell is not None:
#     print(tiny_hut_spell)
#     tiny_hut_spell.prettify_soup()
#     save_object(tiny_hut_spell)

# fireball_spell = load_object('Fireball', 'Spell')
# if fireball_spell is not None:
#     print(fireball_spell)
#     fireball_spell.prettify_soup()
#     save_object(fireball_spell)

