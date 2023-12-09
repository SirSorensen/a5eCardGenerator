


#extract_spells_from_magic_item_table_test(1, True, True)
#prettify_spells_test(list_of_spells)

from data_forge.controller import Controller
from data_forge.data_structures.spell import Spell

controller = Controller()
controller.update_all_tables(Spell.__name__)