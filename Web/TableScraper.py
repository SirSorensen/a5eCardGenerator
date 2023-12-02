

from FileHandler.FileHandler import write_to_file
from Web.TableExtractor import TableExtractor
from Web import a5eScraper


class TableScraper:
    def __init__(self):
        self.url = "spells?combine=&field_spell_ritual_value=All&page="
        self.page = 1
        self.output_filepath = r"Lists\\"
        self.table_extractors : list[TableExtractor] = []

    def scrape_table(self) -> str:
        return a5eScraper.a5e_scrape_source_text(str(self.page), self.url, self.output_filepath)

    def extract_table(self, filepath : str) -> str:
        self.table_extractors.append(TableExtractor(filepath))

        table_extractor = self.table_extractors[-1]

        table_extractor.prettify_soup()
        list_of_names = '\n'.join(table_extractor.extract_list_of_names())

        filepath = f"Outputs\\Lists\\Spells\\{self.page}.txt"
        write_to_file(filepath, list_of_names)

        return list_of_names
    
    def get_all_lists_test(self) -> str:
        is_next_page, next_page_url = self.table_extractors[-1].is_next_page()
        if is_next_page: self.page += 1
        print(is_next_page, next_page_url)


        