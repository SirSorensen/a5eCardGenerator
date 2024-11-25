# TODO: Move everything here to appropriate files to better the structure of the project

from data_forge.controller import Controller
from data_forge.data_structures.combat_maneuver import CombatManeuver
from data_forge.data_structures.magic_item import MagicItem
from data_forge.data_structures.monster import Monster
from data_forge.data_structures.spell import Spell
from data_forge.data_structures.feat import Feat
from data_forge.file_handlers.file_cleaner import FileCleaner

card_types = [CombatManeuver.__name__, Monster.__name__, Feat.__name__, Spell.__name__, MagicItem.__name__,]

# Update all tables for a given card type
def update_all_tables(card_type : str):
    controller = Controller(card_type)
    controller.update_all_tables()

# Update all tables for all card types
def update_all_tables_all_types():
    for card_type in card_types:
        update_all_tables(card_type)

# Update all cards in all saved tables of a given card type
def update_all_cards(card_type : str, controller : Controller = None) -> Controller:
    if controller == None:
        controller : Controller = Controller(card_type)
    else:
        controller.card_type = card_type
    
    controller.update_all_cards()
    return controller

# Update all cards in all saved tables of all card types
def update_all_cards_all_types() -> Controller:
    controller = Controller("")
    for card_type in card_types:
        update_all_cards(card_type, controller=controller)
    return controller

# Do everything above and delete previously generated files (not source code)
def clean_up_and_remake_data(should_clean_up : bool = True) -> Controller:
    if should_clean_up:
        FileCleaner.clean_generated_files()
    update_all_tables_all_types()
    controller = update_all_cards_all_types()
    controller.dump_cards()
