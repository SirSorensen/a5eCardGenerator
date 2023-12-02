

import time
from Web_n_Data.File_Handlers.FileHandler import write_to_file
from Web_n_Data.Data_Interpreters.TableExtractor import TableExtractor
from Web_n_Data.Web_Scrapers import a5eScraper


class TableScraper:
    def __init__(self):
        self.url = "spells?combine=&field_spell_ritual_value=All&page="
        self.page = 0
        self.output_filePath = r'Web_n_Data\\Outputs\\Lists\\Spells\\'
        self.scrape_output_filepath = r"Lists\\Spells\\"
        self.table_extractors : list[TableExtractor] = []

    def scrape_table(self) -> str:
        return a5eScraper.a5e_scrape_source_text(str(self.page), self.url, self.scrape_output_filepath)

    def get_table_extractor(self, index : int) -> TableExtractor:
        return self.table_extractors[index]

    def get_all_tables(self) -> str:
        self.scrape_table()
        is_next_page = self.table_extractors[-1].is_next_page()
        if is_next_page: 
            self.page += 1
            self.get_all_tables()
    

        


        