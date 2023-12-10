


#extract_spells_from_magic_item_table_test(1, True, True)
#prettify_spells_test(list_of_spells)

from data_forge.controller import Controller
from data_forge.data_structures.spell import Spell

controller = Controller(Spell.__name__)
controller.update_all_tables()
controller.update_all_cards()