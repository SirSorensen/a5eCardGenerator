import json
from data_forge.data_interpreters.table_interpreter import TableInterpreter
from data_forge.sheet_maker import SheetMaker
from data_forge.source_code_handlers.source_code import SourceCode
from data_forge.file_handlers.object_handler import ObjectHandler
from data_forge.file_handlers.file_handler import FileHandler

from data_forge.data_structures.card import Card
from data_forge.data_structures.combat_maneuver import CombatManeuver
from data_forge.data_structures.magic_item import MagicItem
from data_forge.data_structures.monster import Monster
from data_forge.data_structures.spell import Spell
from data_forge.data_structures.feat import Feat

from data_forge.settings import *


class Controller:
    def __init__(self, card_type : str, should_load : bool = True):
        self.card_type = card_type
        if should_load:
            self.card_collection = ObjectHandler.load_object(ObjectHandler.gen_pickled_card_dict_filepath())
            if self.card_collection is None:
                self.card_collection = {}
        else:
            self.card_collection = {}


    def get_card(self, title : str) -> Card:
        card_name = Card.to_context_name(title)
        return self.card_collection[card_name]


    def update_card(self, id : str, title : str, summary : str  = "") -> Card:
        if debug: print(f"\nUpdating {self.card_type} card {title}...")
        context_name = Card.to_context_name(title)

        card = self.card_collection.get(context_name)

        if card is None:
            card_stripped_code_path = FileHandler.gen_card_stripped_code_directory(self.card_type, context_name)
            card_stripped_code = FileHandler.read_file(card_stripped_code_path)
            match self.card_type:
                case Spell.__name__:
                    card = Spell(
                        id=id,
                        title=title,
                        source_code=card_stripped_code,
                        summary=summary
                    )
                case Feat.__name__:
                    card = Feat(
                        id=id,
                        title=title,
                        source_code=card_stripped_code
                    )
                case CombatManeuver.__name__:
                    card = CombatManeuver(
                        id=id,
                        title=title,
                        source_code=card_stripped_code,
                        summary=summary
                    )
                case MagicItem.__name__:
                    card = MagicItem(
                        id=id,
                        title=title,
                        source_code=card_stripped_code
                    )
                case Monster.__name__:
                    card = Monster(
                        id=id,
                        title=title,
                        source_code=card_stripped_code
                    )
                case _:
                    raise ValueError(f"ERROR! {self.card_type} is not a valid type!")

            # Save card to card collection    
            self.card_collection[context_name] = card
        
            # Save card str to file
            card_str_path = FileHandler.gen_card_str_directory(self.card_type, context_name)
            FileHandler.write_to_file_if_not_exists(str(card), card_str_path)

            # Save card to pickled object
            ObjectHandler.save_card_if_not_exists(card)

        return card

    def update_all_cards(self, starting_page : int = 0):
        table_interpreter : TableInterpreter = SourceCode.update_cards_from_table_file(self.card_type, starting_page)

        list_of_titles = table_interpreter.extract_list_of_names_with_link()
        
        list_of_summaries = table_interpreter.extract_list_of_summaries(self.card_type)
        has_summaries = len(list_of_summaries) > 0
        
        for i in range(len(list_of_titles)):
            card_title = list_of_titles[i][0]
            card_id = list_of_titles[i][1]

            if has_summaries:
                self.update_card(card_id, card_title, list_of_summaries[i])
            else:
                self.update_card(card_id, card_title)
        
        if table_interpreter.is_next_page():
            self.update_all_cards(starting_page + 1)
        else: 
            print(f"\nFinished updating all {self.card_type} card(s).\n{len(self.card_collection)} card(s) in card_collection.")
            ObjectHandler.save_object(self.card_collection, ObjectHandler.gen_pickled_card_dict_filepath())
        


    # Update the file for the table with the given page number and card type. 
    # Returns the TableInterpreter for the relevant table.
    def update_table(self, page_number : int) -> bool:
        # Scrape source text of table
        source_code = SourceCode.update_table_source_code(self.card_type, page_number)

        # Return is_next_page
        return TableInterpreter(source_code).is_next_page()


    # Update all files for tables with the given card type. 
    # Returns nothing.
    def update_all_tables(self, starting_page : int = 0):
        # Update the table at current page.
        is_next_page = self.update_table(starting_page)

        # If there is a next page after the current table's, then continue.
        if is_next_page:
            self.update_all_tables(starting_page + 1)
        else:
            if debug: print(f"\nFinished scraping {self.card_type} tables. {starting_page+1} page(s) scraped.")
    
    def get_list_of_card(self, card_type : str) -> list:
        card_values = self.card_collection.values()
        print("Amount of card_values:" + str(len(card_values)))
        cards_of_card_type = list(filter(lambda c: type(c).__name__ == card_type, card_values))
        print("Amount of cards_of_card_type:" + str(len(cards_of_card_type)))
        return cards_of_card_type

    def get_cards(self, input_list) -> list:
        card_list = []
        for amount, name in input_list:
            for _ in range(amount):
                card_list.append(self.get_card(name))
        return card_list

    def read_input(self) -> list:
        sheet_maker = SheetMaker(r'Resources/Cards.xlsm', read=True)
        inputs = sheet_maker.read_input()

        if debug:
            print("Read Input:")
            for input in inputs:
                print(str(input))

        cards = self.get_cards(inputs)
        
        if debug:
            print("Cards Found:")
            for card in cards:
                print(str(card.title))

        return cards

    def dump_cards(self):
        card_json = "\"cards\" : ["
        for card in self.card_collection.values():
            card_json += json.dumps(card, default=lambda o: o.__dict__)
            card_json += ",\n"

        card_json = card_json[:-2] + "\n]"

        FileHandler.write_to_file(card_json, FileHandler.gen_json_output_directory())

        print(f"Dumped {len(self.card_collection)} cards to {FileHandler.gen_json_output_directory()}")