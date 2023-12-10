
from data_forge.data_structures.context import Context
from data_forge.file_handlers.file_handler import FileHandler
from data_forge.web_scrapers.website_scraper import scrape_table_source_code, scrape_source_text
from data_forge.data_interpreters.table_interpreter import TableInterpreter

class SourceCode:

    def update_table_source_code(card_type : str, page_number : str) -> str:
        print(f"\nUpdating {card_type}-table, page {page_number}.")

        # Scrape table source code if it doesn't exist yet
        card_list_source_code_path = FileHandler.get_card_list_source_code_directory(card_type, page_number)
        if not FileHandler.does_file_exist(card_list_source_code_path):
            source_code = scrape_table_source_code(card_type, page_number)
        else:
            source_code = ""        
        source_code = FileHandler.write_to_file_if_not_exists(source_code, card_list_source_code_path)

        # Prettify table source code if it doesn't exist yet
        card_list_pretty_code_path = FileHandler.get_card_list_pretty_code_directory(card_type, page_number)
        if not FileHandler.does_file_exist(card_list_pretty_code_path):
            pretty_code = TableInterpreter.prettify_html_source_code(source_code)
        else:
            pretty_code = ""
        pretty_code = FileHandler.write_to_file_if_not_exists(pretty_code, card_list_pretty_code_path)

        # Return table source code 
        return source_code
    

    # Update a card from a type, a name & url ending
    def update_card(card_type : str, card_name : str, card_url_ending : str) -> str:
        print(f"\nUpdating {card_type} card \'{card_name}\'.")

        # Scrape card source code
        context_name = Context.name_to_data_name(card_name)
        card_source_code_path = FileHandler.get_card_source_code_directory(card_type, context_name)
        if not FileHandler.does_file_exist(card_source_code_path):
            card_source_code = scrape_source_text(card_url_ending)
        else:
            card_source_code = ""
        card_source_code = FileHandler.write_to_file_if_not_exists(card_source_code, card_source_code_path)

        # Prettify card source code
        card_pretty_code_path = FileHandler.get_card_pretty_code_directory(card_type, context_name)
        if not FileHandler.does_file_exist(card_pretty_code_path):
            card_pretty_code = TableInterpreter.prettify_html_source_code(card_source_code)
            FileHandler.write_to_file(card_pretty_code, card_pretty_code_path)
        
        # Return card source code
        return card_source_code
    

    # Update all cards from a list of names & url endings
    def update_card_from_list(card_type : str, list_of_names : list[str]):
        for i in range(len(list_of_names)):
            card_name = list_of_names[i][0]
            card_url_ending = list_of_names[i][1]
            SourceCode.update_card(card_type, card_name, card_url_ending)