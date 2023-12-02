from Data_Structures.Spell import Spell

#spell_source_text = scrape_spell("Abstraction")
#print("Encoding = " + spell_source_text.encoding)

abstraction_spell = Spell(web_location="abstraction")

print(abstraction_spell)
abstraction_spell.prettify_soup()
