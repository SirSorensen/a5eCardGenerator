from Data_Structures.Spell import Spell
from Data_Structures.Spell import read_spell_file
from Data_Structures.Spell import scrape_spell

#spell_source_text = scrape_spell("Abstraction")
#print("Encoding = " + spell_source_text.encoding)

spell_source_text = read_spell_file("abstraction")

abstraction_spell = Spell(source_text=spell_source_text)

abstraction_spell.extract_spell(spell_source_text)

print("Done!")