
from data_forge.data_structures.card_data import CardData
from data_forge.file_handlers.file_handler import FileHandler
from data_forge.web_scrapers.website_scraper import scrape_table_source_code, scrape_source_text
from data_forge.data_interpreters.table_interpreter import TableInterpreter

class SourceCode:

    def update_table_source_code(card_type : str, page_number : str) -> str:
        print(f"\nUpdating {card_type}-table, page {page_number}.")

        if not FileHandler.does_card_list_source_code_exist(card_type, page_number):
            source_code = scrape_table_source_code(card_type, page_number)
            FileHandler.save_card_list_source_code(source_code, card_type, page_number)
        else:
            source_code = FileHandler.read_card_list_source_code(card_type, page_number)

        return source_code
    
    def update_card(card_type : str, card_name : str, card_url_ending : str):
        print(f"\nUpdating {card_type} card \'{card_name}\'.")
        # Scrape card source code
        card_data_name = CardData.name_to_data_name(card_name)
        if not FileHandler.does_card_source_code_exist(card_type, card_data_name):
            card_source_code = scrape_source_text(card_url_ending)
            FileHandler.write_to_file_absolute_path(card_source_code, FileHandler.get_card_source_code_directory())
        else:
            card_source_code = FileHandler.read_card_source_code(card_type, card_data_name)

        # Prettify card source code
        if not FileHandler.does_card_pretty_code_exist(card_type, card_data_name):
            card_pretty_code = TableInterpreter.prettify_html_source_code(card_source_code)
            FileHandler.save_card_pretty_code(card_pretty_code, card_type, card_data_name)
    
    def update_card_from_list(card_type : str, list_of_names : list[str]):
        for i in range(len(list_of_names)):
            card_name = list_of_names[i][0]
            card_url_ending = list_of_names[i][1]
            SourceCode.update_card(card_type, card_name, card_url_ending)