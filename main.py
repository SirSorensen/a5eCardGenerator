from Data_Structures.Spell import Spell
from Data_Structures.Spell import read_spell_file


spell_source_text = read_spell_file("abstraction")

abstraction_spell = Spell(source_text=spell_source_text)

abstraction_spell.extract_spell(spell_source_text)