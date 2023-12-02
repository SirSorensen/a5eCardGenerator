
from Web.TableScraper import TableScraper
from tests import load_saved_spells_test



list_scraper = TableScraper()
filepath = list_scraper.scrape_table()
print("Filepath:", filepath)
list_scraper.extract_table("Outputs\\Lists\\source_text_1.txt")

next_list = list_scraper.get_all_lists_test()


# load_saved_spells_test()
