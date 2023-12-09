




from data_forge.data_interpreters.table_interpreter import TableInterpreter
from data_forge.data_structures.card import Card
from data_forge.data_structures.magic_item import MagicItem
from data_forge.data_structures.spell import Spell
from data_forge.web_scrapers.website_scraper import scrape_table_source_text
from data_forge.file_handlers.file_handler import FileHandler


class Controller:
    def __init__(self):
        pass

    def get_card(name : str, type : str) -> Card:
        pass
    
    def update_card(name : str, type : str) -> Card:
        pass


    # Update the file for the table with the given page number and card type. 
    # Returns the TableInterpreter for the relevant table.
    def update_table(self, card_type : str, page_number : int) -> TableInterpreter:
        # Scrape source text of table
        source_text = scrape_table_source_text(card_type, page_number)
        FileHandler.save_card_list_source_code(card_type, page_number, source_text)
        
        # Make TableInterpreter for table
        table_interpreter = TableInterpreter(source_text)
        FileHandler.save_card_list_pretty_code(card_type, page_number, table_interpreter.prettify_html())
        
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
            self.update_all_tables(card_type, starting_page + 1)
        else:
            print(f"\nFinished scraping {card_type} tables. {starting_page+1} page(s) scraped.")
    

