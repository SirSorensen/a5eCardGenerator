# TODO: Move everything here to appropriate files to better the structure of the project

from data_forge.controller import Controller
from data_forge.data_structures.combat_maneuver import CombatManeuver
from data_forge.data_structures.magic_item import MagicItem
from data_forge.data_structures.monster import Monster
from data_forge.data_structures.spell import Spell
from data_forge.data_structures.feat import Feat
from data_forge.file_handlers.file_cleaner import FileCleaner
from data_forge.sheet_maker import SheetMaker

card_types = [CombatManeuver.__name__, Monster.__name__, Feat.__name__, Spell.__name__, MagicItem.__name__,]

# Update data
def test_update_all_tables(card_type : str) -> Controller:
    controller = Controller(card_type)
    controller.update_all_tables()

def test_update_all_tables_all_types():
    for card_type in card_types:
        test_update_all_tables(card_type)

def test_update_all_cards(card_type : str, controller = None) -> Controller:
    if controller == None:
        controller = Controller(card_type)
    else:
        controller.card_type = card_type
    
    controller.update_all_cards()
    return controller

def test_update_all_cards_all_types() -> Controller:
    controller = Controller("")
    for card_type in card_types:
        test_update_all_cards(card_type, controller=controller)
    return controller


def clean_up_and_remake_data(should_clean_up : bool = True):
    if should_clean_up:
        FileCleaner.clean_generated_files()
    test_update_all_tables_all_types()
    controller = test_update_all_cards_all_types(should_load=not should_clean_up)
    #test_insert_all_cards_in_sheet_all_types()
    controller.dump_cards()




# Test sheet_maker
def test_insert_all_cards_in_sheet(sheet_maker : SheetMaker, card_type : str, controller = None):
    if controller == None:
        controller = Controller(card_type)
    
    sheet_maker.add_card_sheet(card_type)
    cards = controller.get_list_of_card(card_type)

    for card in cards:
        sheet_maker.insert_card_properties(card)
    
    sheet_maker.gen_name_list(len(cards))

def test_insert_all_cards_in_sheet_all_types():
    sheet_maker = SheetMaker()
    controller = Controller(Spell.__name__)

    test_insert_all_cards_in_sheet(sheet_maker, CombatManeuver.__name__, controller=controller)
    test_insert_all_cards_in_sheet(sheet_maker, Feat.__name__, controller=controller, )
    test_insert_all_cards_in_sheet(sheet_maker, MagicItem.__name__, controller=controller)
    test_insert_all_cards_in_sheet(sheet_maker, Monster.__name__, controller=controller)
    test_insert_all_cards_in_sheet(sheet_maker, Spell.__name__, controller=controller)

    sheet_maker.save()

def test_input() -> list:    
    controller = Controller("")
    return controller.read_input()


# Test power_point_modifier
def test_insert_input_into_power_point():
    cards = test_input()
    power_point_modifier = PowerPointModifier()
    for card in cards:
        power_point_modifier.insertCard(card)
    power_point_modifier.save()