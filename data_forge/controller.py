




from data_forge.data_interpreters.table_interpreter import TableInterpreter
from data_forge.data_structures.card import Card
from data_forge.data_structures.card_data import CardData
from data_forge.data_structures.magic_item import MagicItem
from data_forge.data_structures.spell import Spell
from data_forge.table_to_data_structure import TableToDataStructure
from data_forge.web_scrapers.website_scraper import scrape_table_source_text, scrape_source_text
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
    def update_table(self, card_type : str, page_number : int) -> TableInterpreter:
        print(f"\nUpdating {card_type}-table, page {page_number}.")
        # Scrape source text of table
        if not FileHandler.does_card_list_source_code_exist(card_type, page_number):
            source_text = scrape_table_source_text(card_type, page_number)
            FileHandler.save_card_list_source_code(source_text, card_type, page_number)
        else:
            source_text = FileHandler.read_card_list_source_code(card_type, page_number)
        
        # Make TableInterpreter for table
        table_interpreter = TableInterpreter(source_text)
        FileHandler.save_card_list_pretty_code(table_interpreter.prettify_html(), card_type, page_number)

        # Scrape cards
        print(f"\nUpdating {card_type} cards, from table-page {page_number}.")
        list_of_names = table_interpreter.extract_list_of_names_with_link()
        for i in range(len(list_of_names)):
            print(f"\nUpdating {card_type} card \'{list_of_names[i][0]}\'.")
            card_data_name = CardData.name_to_data_name(list_of_names[i][0])

            # Scrape card source code
            if not FileHandler.does_card_source_code_exist(card_type, card_data_name):
                card_url_ending = list_of_names[i][1]
                card_source_code = scrape_source_text(card_url_ending)
                FileHandler.save_card_source_code(card_source_code, card_type, card_data_name)
            else:
                card_source_code = FileHandler.read_card_source_code(card_type, card_data_name)

            # Prettify card source code
            if not FileHandler.does_card_pretty_code_exist(card_type, card_data_name):
                card_pretty_code = TableInterpreter.prettify_html_source_code(card_source_code)
                FileHandler.save_card_pretty_code(card_pretty_code, card_type, card_data_name)

        # Make cards
        table_to_data_structure = TableToDataStructure(card_type)
        card_contexts = table_to_data_structure.make_data_structures(table_interpreter)
        for card in card_contexts:
            FileHandler.save_card_str(card)

        # Return TableExtractor of table
        return table_interpreter


    # Update all files for tables with the given card type. 
    # Returns nothing.
    def update_all_tables(self, card_type : str, starting_page : int = 0):
        # Update the table at current page.
        table_interpreter : TableInterpreter = self.update_table(card_type, starting_page)

        # If there is a next page after the current table's, then continue.
        is_next_page = table_interpreter.is_next_page()
        if is_next_page:
            return self.update_all_tables(card_type, starting_page + 1)
        else:
            print(f"\nFinished scraping {card_type} tables. {starting_page+1} page(s) scraped.")
    

