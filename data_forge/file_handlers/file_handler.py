import os
import re

global_output_directory = r"Outputs/"
global_source_code_output_directory = rf"{global_output_directory}Source_Code/"
global_list_output_directory = rf"{global_source_code_output_directory}Lists/"

class FileHandler:

    # Returns the contents of the file with file path = abs_filepath
    def read_file(abs_filepath : str) -> str:
        if os.path.exists(abs_filepath):
            with open(abs_filepath, "r", encoding='utf-8') as file:
                content = file.read()
                file.close()
        else:
            print(f"File not found: {abs_filepath}")
            content = ""

        return content        

    # Returns the contents of the written file
    def write_to_file(content:str, output_abs_filepath:str):
        print(f"Writing to {output_abs_filepath}...")
        
        # Create the file if it doesn't exist
        FileHandler._make_file_if_not_exists(output_abs_filepath)
        
        # Write the content to the file
        with open(output_abs_filepath, "w+", encoding='utf-8') as file:
            file.write(content)
            file.close()
        
        return content

    # Returns the contents of the written file, or the contents of the file if it already exists
    def write_to_file_if_not_exists(content:str, abs_filepath:str):
        if not FileHandler.does_file_exist(abs_filepath):
            return FileHandler.write_to_file(content, abs_filepath)
        else:
            return FileHandler.read_file(abs_filepath)


    def _make_file_if_not_exists(output_abs_filepath:str) -> str:
        if not os.path.exists(output_abs_filepath):
            os.makedirs(os.path.dirname(output_abs_filepath), exist_ok=True)
            with open(output_abs_filepath, "w") as f: pass
        return output_abs_filepath
    

    def does_file_exist(abs_filepath : str) -> bool:
        result = os.path.exists(abs_filepath)
        if result: 
            print(f"{abs_filepath} already exists.")
        return result



    
    def get_card_source_code_directory(card_type : str, card_data_name : str):
        return rf"{global_source_code_output_directory}{card_type}s/source_code_{card_data_name}.html"
    

    def get_card_pretty_code_directory(card_type : str, card_data_name : str) -> str:
        return rf"{global_source_code_output_directory}{card_type}s/Pretty/pretty_code_of_page_{card_data_name}.html"
    
    def get_card_str_directory(card_type : str, card_data_name : str):
        return rf"{global_output_directory}{card_type}s/Strings/{card_data_name}.txt"

    def get_card_list_source_code_directory(card_type : str, page_number : str):
        return rf"{global_list_output_directory}{card_type}s/source_code_of_page_{page_number}.html"

    def get_card_list_pretty_code_directory(card_type : str, page_number : str):
        return rf"{global_list_output_directory}{card_type}s/Pretty/pretty_code_of_page_{page_number}.html"



    

