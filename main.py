from Web import SourceCodeInterpreter
from Web import a5eScraper
from tests import load_saved_spells_test




filepath = a5eScraper.a5e_scrape_source_text("1", "spells?combine=&field_spell_ritual_value=All&page=", r"Lists\\")

code_interpreter = SourceCodeInterpreter.CodeInterpreter(filepath)
code_interpreter.prettify_soup()

# load_saved_spells_test()
