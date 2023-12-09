from data_forge.data_interpreters.table_extractor import TableExtractor
from data_forge.data_structures.magic_item import MagicItem
from data_forge.data_structures.spell import Spell
from data_forge.web_scrapers import a5eScraper

# This class scrapes and extracts tables from the a5e.tools (such as the spell list or magic item list)
class TableController:
    def __init__(self, card_data_type : str, starting_page : int = 0):
        self.card_data_type = card_data_type
        self.sub_url = self.__get_sub_url()

        # Output file path for the scraped HTML
        self.output_filePath = f'Outputs\\Lists\\{card_data_type}s\\source_text_'

        self.current_page = starting_page
        self.table_extractor : TableExtractor = None


    def get_all_tables(self) -> str:
        self.__scrape_table()
        self.table_extractor = self.__extract_table()
        is_next_page = self.table_extractor.is_next_page()
        if is_next_page: 
            self.current_page += 1
            self.get_all_tables()
        else:
            print(f"\nFinished scraping {self.card_data_type} tables. {self.current_page+1} page(s) scraped.")


    def __scrape_table(self) -> str:
        return a5eScraper.a5e_scrape_source_text(str(self.current_page), self.output_filePath, sub_url=self.sub_url)


    def __extract_table(self):
        return TableExtractor(self.output_filePath, self.current_page, ".html")

    
    def __get_sub_url(self):
        match self.card_data_type:
            case Spell.__name__:
                return r"spells?combine=&field_spell_ritual_value=All&page="
            case MagicItem.__name__:
                return r"magic-items?field_mi_cost_value%5Bmin%5D=&field_mi_cost_value%5Bmax%5D=&combine=&page="
            case _:
                raise ValueError(f"Card data type {self.card_data_type} is not supported by TableScraper.py")
            

    

        


        