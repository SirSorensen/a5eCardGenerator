from data_forge.controller import Controller
from data_forge.data_structures.combat_maneuver import CombatManeuver
from data_forge.data_structures.magic_item import MagicItem
from data_forge.data_structures.monster import Monster
from data_forge.data_structures.spell import Spell
from data_forge.data_structures.feat import Feat
from data_forge.file_handlers.file_cleaner import FileCleaner

card_types = [CombatManeuver.__name__, Monster.__name__, Feat.__name__, Spell.__name__, MagicItem.__name__,]

def test_update_all_tables(card_type : str) -> Controller:
    controller = Controller(card_type)
    controller.update_all_tables()

def test_update_all_tables_all_types():
    for card_type in card_types:
        test_update_all_tables(card_type)


def test_update_all_cards(card_type : str) -> Controller:
    controller = Controller(card_type)
    controller.update_all_cards()
    return controller

def test_update_all_cards_all_types():
    for card_type in card_types:
        test_update_all_cards(card_type)


def test_input(controller : Controller):
    # print(str(controller.get_card("Acid Arrow")))
    card_name = input("Enter card name: ")
    controller.get_card(card_name)



# Insert runs below


FileCleaner.clean_generated_files()
# FileCleaner.move_old_files()

test_update_all_tables_all_types()
test_update_all_cards_all_types()

# test_update_all_tables(Feat.__name__)
# test_update_all_tables(CombatManeuver.__name__)
# test_update_all_tables(MagicItem.__name__)
# test_update_all_tables(Monster.__name__)
# test_update_all_tables(Spell.__name__)



# controller = Controller(MagicItem.__name__)

# for key in controller.card_collection.keys():
#     print(key)