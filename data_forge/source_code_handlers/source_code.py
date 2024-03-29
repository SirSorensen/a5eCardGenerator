
from data_forge.source_code_handlers.website_scraper import scrape_table_source_code, scrape_source_code, gen_card_url, gen_table_url
from data_forge.data_interpreters.context_interpreter import ContextInterpreter
from data_forge.data_interpreters.table_interpreter import TableInterpreter
from data_forge.file_handlers.file_handler import FileHandler
from data_forge.data_structures.card import Card

from data_forge.settings import *

class SourceCode:

    def update_table_source_code(card_type : str, page_number : str) -> str:
        print(f"\nUpdating files for {card_type} table, page {page_number}. (See {gen_table_url(card_type, page_number)} for source.)")

        # Scrape table source code if it doesn't exist yet
        card_list_source_code_path = FileHandler.gen_card_list_source_code_directory(card_type, page_number)
        if not FileHandler.does_file_exist(card_list_source_code_path):
            table_source_code = scrape_table_source_code(card_type, page_number)
        else:
            table_source_code = ""        
        table_source_code = FileHandler.write_to_file_if_not_exists(table_source_code, card_list_source_code_path)

        # Set up TableInterpreter
        table_interpreter = TableInterpreter(table_source_code)

        # Prettify table source code
        table_pretty_code_path = FileHandler.gen_card_list_source_code_directory(card_type, page_number, is_pretty=True)
        table_pretty_code = SourceCode.__process_code(table_pretty_code_path, table_interpreter.get_pretty_code)

        # Generate/find table stripped code
        table_stripped_code_path = FileHandler.gen_card_list_source_code_directory(card_type, page_number, is_stripped=True)
        table_stripped_code = SourceCode.__process_code(table_stripped_code_path, table_interpreter.get_stripped_code)

        # Prettify table stripped code
        table_stripped_pretty_path = FileHandler.gen_card_list_source_code_directory(card_type, page_number, is_stripped=True, is_pretty=True)
        table_stripped_code = SourceCode.__process_code(table_stripped_pretty_path, table_interpreter.get_pretty_stripped_code)

        # Return table source code 
        return table_source_code
    

    # Update a card from a type, a name & url ending
    def update_card_source_code(card_type : str, card_name : str, card_url_ending : str) -> str:
        print(f"\nUpdating files for {card_type} card \'{card_name}\'. (See {gen_card_url(card_url_ending)} for source.)")

        # Scrape card source code
        context_name = Card.to_context_name(card_name)
        card_source_code_path = FileHandler.gen_card_source_code_directory(card_type, context_name)
        if not FileHandler.does_file_exist(card_source_code_path):
            card_source_code = scrape_source_code(card_url_ending)
        else:
            card_source_code = ""
        card_source_code = FileHandler.write_to_file_if_not_exists(card_source_code, card_source_code_path)

        # Set up CodeInterpreter
        context_interpreter = ContextInterpreter(card_source_code)

        # Prettify card source code
        card_pretty_code_path = FileHandler.gen_card_source_code_directory(card_type, context_name, is_pretty=True)
        card_pretty_code = SourceCode.__process_code(card_pretty_code_path, context_interpreter.get_pretty_code)
        
        # Generate/find card stripped code
        card_stripped_code_path = FileHandler.gen_card_stripped_code_directory(card_type, context_name)
        card_stripped_code = SourceCode.__process_code(card_stripped_code_path, context_interpreter.get_stripped_code)

        # Prettify card stripped code
        card_pretty_stripped_path = FileHandler.gen_card_stripped_code_directory(card_type, context_name, is_pretty=True)
        card_pretty_stripped = SourceCode.__process_code(card_pretty_stripped_path, context_interpreter.get_pretty_stripped_code)

        # Return card stripped code
        return card_stripped_code

    
    # Update all cards from a list of names & url endings
    def update_card_table_source_code(card_type : str, list_of_names : list[str]):
        for i in range(len(list_of_names)):
            card_name = list_of_names[i][0]
            card_url_ending = list_of_names[i][1]
            SourceCode.update_card_source_code(card_type, card_name, card_url_ending)
    
    def update_cards_from_table_file(card_type : str, page_number : int) -> TableInterpreter:
        # Make TableInterpreter for table
        table_abs_filepath = FileHandler.gen_card_list_source_code_directory(card_type, page_number)
        table_source_code = FileHandler.read_file(table_abs_filepath)
        table_interpreter = TableInterpreter(table_source_code)

        # Scrape cards
        list_of_titles = table_interpreter.extract_list_of_names_with_link()
        print(f"\nUpdating {len(list_of_titles)} {card_type} card files, from table-page {page_number}. (See {gen_table_url(card_type, page_number)} for source.)")
        SourceCode.update_card_table_source_code(card_type, list_of_titles)

        return table_interpreter
    

    # Function to handle prettifying and extracting stripped code
    def __process_code(file_path: str, processing_func):
        if not FileHandler.does_file_exist(file_path):
            processed_code = processing_func()
        else:
            processed_code = ""
        return FileHandler.write_to_file_if_not_exists(processed_code, file_path)