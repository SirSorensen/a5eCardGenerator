import os
import re

global_output_directory = r"Outputs/"
global_list_output_directory = rf"{global_output_directory}Lists/"

class FileHandler:

    # Returns the contents of the file with file path = abs_filepath
    def read_file(abs_filepath):
        if os.path.exists(abs_filepath):
            with open(abs_filepath, "r", encoding='utf-8') as file:
                content = file.read()
                file.close()
        else:
            print(f"File not found: {abs_filepath}")
            content = ""

        return content

    # Returns the absolute path of the written file
    def write_to_file_absolute_path(content:str, output_abs_filepath:str, file_extension:str = "") -> str:
        output_abs_filepath = rf"{output_abs_filepath}{file_extension}"
        FileHandler.__write_to_file(content, output_abs_filepath)
        return output_abs_filepath
        

    # Returns the absolute path of the written file
    def __write_to_file(content:str, output_abs_filepath:str):
        print(f"Writing to {output_abs_filepath}...")
        
        # Create the file if it doesn't exist
        FileHandler._make_file_if_not_exists(output_abs_filepath)
        
        # Write the content to the file
        with open(output_abs_filepath, "w+", encoding='utf-8') as file:
            file.write(content)


    def _make_file_if_not_exists(output_abs_filepath:str) -> str:
        print(f"output_abs_filepath = {output_abs_filepath}")
        if not os.path.exists(output_abs_filepath):
            os.makedirs(os.path.dirname(output_abs_filepath), exist_ok=True)
            with open(output_abs_filepath, "w") as f: pass
        return output_abs_filepath
    

    def save_card_source_code(card_type : str, file_name : str, content:str) -> str:
        # Set output_directory
        output_directory = rf"{global_output_directory}{card_type}s/source_text_{file_name}.html"
        
        return FileHandler.write_to_file_absolute_path(content, output_directory, r'.html')
    
    def save_card_list_source_code(card_type : str, page_number : str, content:str) -> str:
        # Set output_directory
        output_directory = rf"{global_list_output_directory}{card_type}s/source_code_of_page_{page_number}"
        
        return FileHandler.write_to_file_absolute_path(content, output_directory, r'.html')
    
    def save_card_list_pretty_code(card_type : str, page_number : str, content:str) -> str:
        # Set output_directory
        output_directory = rf"{global_list_output_directory}{card_type}s/Pretty/pretty_code_of_page_{page_number}"
        
        return FileHandler.write_to_file_absolute_path(content, output_directory, r'.html')