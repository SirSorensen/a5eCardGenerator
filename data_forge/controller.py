




from data_forge.data_interpreters.table_interpreter import TableInterpreter
from data_forge.data_structures.card import Card
from data_forge.data_structures.card_data import CardData
from data_forge.data_structures.magic_item import MagicItem
from data_forge.data_structures.spell import Spell
from data_forge.source_code import SourceCode
from data_forge.table_to_data_structure import TableToDataStructure
from data_forge.web_scrapers.website_scraper import scrape_table_source_code, scrape_source_text
from data_forge.file_handlers.file_handler import FileHandler


class Controller:
    def __init__(self):
        pass

    def get_card(name : str, card_type : str) -> Card:
        pass
    
    def update_card(name : str, card_type : str) -> Card:
        pass


    def update_all_cards(card_type : str):
        pass


    # Update the file for the table with the given page number and card type. 
    # Returns the TableInterpreter for the relevant table.
    def update_table(self, card_type : str, page_number : int) -> bool:
        # Scrape source text of table
        source_code = SourceCode.update_table_source_code(card_type, page_number)
        
        # Make TableInterpreter for table
        table_interpreter = TableInterpreter(source_code)
        FileHandler.save_card_list_pretty_code(table_interpreter.prettify_html(), card_type, page_number)

        # Scrape cards
        print(f"\nUpdating {card_type} cards, from table-page {page_number}.")
        list_of_names = table_interpreter.extract_list_of_names_with_link()
        SourceCode.update_card_from_list(card_type, list_of_names)

        # Make cards
        # table_to_data_structure = TableToDataStructure(card_type)
        # card_contexts = table_to_data_structure.make_data_structures(table_interpreter)
        # for card in card_contexts:
        #     FileHandler.save_card_str(card)

        # Return TableExtractor of table
        return table_interpreter.is_next_page()


    # Update all files for tables with the given card type. 
    # Returns nothing.
    def update_all_tables(self, card_type : str, starting_page : int = 0):
        # Update the table at current page.
        is_next_page = self.update_table(card_type, starting_page)

        # If there is a next page after the current table's, then continue.
        if is_next_page:
            self.update_all_tables(card_type, starting_page + 1)
        else:
            print(f"\nFinished scraping {card_type} tables. {starting_page+1} page(s) scraped.")
    

