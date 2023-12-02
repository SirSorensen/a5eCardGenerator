

import time
from FileHandler.FileHandler import write_to_file
from Data_Interpreters.TableExtractor import TableExtractor
from Web_Scrapers import a5eScraper


class TableScraper:
    def __init__(self):
        self.url = "spells?combine=&field_spell_ritual_value=All&page="
        self.page = 0
        self.output_filePath = r'Outputs\\Lists\\Spells\\'
        self.scrape_output_filepath = r"Lists\\Spells\\"
        self.table_extractors : list[TableExtractor] = []

    def scrape_table(self) -> str:
        return a5eScraper.a5e_scrape_source_text(str(self.page), self.url, self.scrape_output_filepath)

    def extract_table(self, filepath : str) -> str:
        self.table_extractors.append(TableExtractor(filepath))

        table_extractor = self.table_extractors[-1]

        table_extractor.prettify_soup()
        list_of_names = '\n'.join(table_extractor.extract_list_of_names())

        filepath = f"{self.output_filePath}Names\\{self.page}.txt"
        write_to_file(filepath, list_of_names)

        return list_of_names
    
    def get_all_tables(self) -> str:
        self.scrape_table()
        self.extract_table(f"{self.output_filePath}source_text_{self.page}.txt")
        is_next_page = self.table_extractors[-1].is_next_page()
        if is_next_page: 
            self.page += 1
            time.sleep(2)
            self.get_all_tables()
    

        


        