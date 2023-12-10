




from data_forge.data_interpreters.table_interpreter import TableInterpreter
from data_forge.data_structures.card import Card
from data_forge.data_structures.combat_maneuver import CombatManeuver
from data_forge.data_structures.card import Card
from data_forge.data_structures.feat import Feat
from data_forge.data_structures.magic_item import MagicItem
from data_forge.data_structures.spell import Spell
from data_forge.source_code import SourceCode
from data_forge.table_to_data_structure import TableToDataStructure
from data_forge.web_scrapers.website_scraper import scrape_table_source_code, scrape_source_text
from data_forge.file_handlers.file_handler import FileHandler


class Controller:
    def __init__(self, card_type : str):
        self.card_type = card_type
        self.card_collection = {}


    def get_card(self, title : str) -> Card:
        pass


    def update_card(self, title : str, summary : str  = "") -> Card:
        print(f"\nUpdating {self.card_type} card {title}...")
        context_name = Card.title_to_context_name(title)
        card_source_code_path = FileHandler.get_card_source_code_directory(self.card_type, context_name)
        card_source_code = FileHandler.read_file(card_source_code_path)
        match self.card_type:
            case Spell.__name__:
                card = Spell(
                    title=title,
                    source_code=card_source_code,
                    summary=summary
                )
            case Feat.__name__:
                card = Feat()
            case CombatManeuver.__name__:
                card = CombatManeuver()
            case MagicItem.__name__:
                card = MagicItem(
                    title=title,
                    source_code=card_source_code
                    )
            case _:
                raise ValueError(f"ERROR! {self.card_type} is not a valid type!")

        # Save card to card collection    
        self.card_collection[context_name] = card
        
        # Save card to file
        card_str_path = FileHandler.get_card_str_directory(self.card_type, context_name)
        FileHandler.write_to_file_if_not_exists(str(card), card_str_path)

        

        return card



    def update_all_cards(self, starting_page : int = 0):
        card_list_source_code_path = FileHandler.get_card_list_source_code_directory(self.card_type, starting_page)
        if FileHandler.does_file_exist(card_list_source_code_path):
            print(f"\nUpdating {self.card_type} cards, from table-page {starting_page}.")
            table_source_code = FileHandler.read_file(card_list_source_code_path)
            table_interpreter = TableInterpreter(table_source_code)
            list_of_titles = table_interpreter.extract_list_of_names_with_link()
            if self.card_type == Spell.__name__:
                list_of_summaries = table_interpreter.extract_list_of_summaries()
            
            for i in range(len(list_of_titles)):
                card_title = list_of_titles[i][0]
                if self.card_type == Spell.__name__:
                    self.update_card(card_title, list_of_summaries[i])
                else:
                    self.update_card(card_title)
            
            self.update_all_cards(starting_page + 1)


    # Update the file for the table with the given page number and card type. 
    # Returns the TableInterpreter for the relevant table.
    def update_table(self, page_number : int) -> bool:
        # Scrape source text of table
        source_code = SourceCode.update_table_source_code(self.card_type, page_number)
        
        # Make TableInterpreter for table
        table_interpreter = TableInterpreter(source_code)

        # Scrape cards
        print(f"\nUpdating {self.card_type} cards, from table-page {page_number}.")
        list_of_titles = table_interpreter.extract_list_of_names_with_link()
        SourceCode.update_card_from_list(self.card_type, list_of_titles)

        # Return TableExtractor of table
        return table_interpreter.is_next_page()


    # Update all files for tables with the given card type. 
    # Returns nothing.
    def update_all_tables(self, starting_page : int = 0):
        # Update the table at current page.
        is_next_page = self.update_table(starting_page)

        # If there is a next page after the current table's, then continue.
        if is_next_page:
            self.update_all_tables(starting_page + 1)
        else:
            print(f"\nFinished scraping {self.card_type} tables. {starting_page+1} page(s) scraped.")
    

