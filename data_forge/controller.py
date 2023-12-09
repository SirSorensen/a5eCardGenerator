




from data_forge.data_interpreters.table_extractor import TableExtractor
from data_forge.data_structures.card import Card
from data_forge.data_structures.magic_item import MagicItem
from data_forge.data_structures.spell import Spell
from data_forge.web_scrapers.website_scraper import scrape_source_text


class Controller:
    def __init__(self):
        pass

    def get_card(name : str, type : str) -> Card:
        pass
    
    def update_card(name : str, type : str) -> Card:
        pass

    def update_table(type : str) -> str:
        pass

    def update_all_tables(self, starting_page : int = 0) -> str:
        scrape_source_text(self.__get_table_sub_url() + str(starting_page))
        table_extractor = TableExtractor(self.__get_table_sub_url(), starting_page, ".html")
        is_next_page = table_extractor.is_next_page()
        if is_next_page: 
            self.update_all_tables(starting_page + 1)
        else:
            print(f"\nFinished scraping {starting_page} tables. {starting_page+1} page(s) scraped.")
    
    
    def __get_table_sub_url(card_data_type, page_number : int = 0):
        match card_data_type:
            case Spell.__name__:
                return r"spells?combine=&field_spell_ritual_value=All&page=" + str(page_number)
            case MagicItem.__name__:
                return r"magic-items?field_mi_cost_value%5Bmin%5D=&field_mi_cost_value%5Bmax%5D=&combine=&page=" + str(page_number)
            case _:
                raise ValueError(f"Card data type {card_data_type} is not supported by TableScraper.py")