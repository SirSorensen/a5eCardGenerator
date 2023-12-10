import os
import re

global_output_directory = r"Outputs/"
global_source_code_output_directory = rf"{global_output_directory}Source_Code/"
global_list_output_directory = rf"{global_source_code_output_directory}Lists/"

class FileHandler:

    # Returns the contents of the file with file path = abs_filepath
    def __read_file(abs_filepath : str) -> str:
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
        if not os.path.exists(output_abs_filepath):
            os.makedirs(os.path.dirname(output_abs_filepath), exist_ok=True)
            with open(output_abs_filepath, "w") as f: pass
        return output_abs_filepath
    

    def __does_file_already_exist(abs_filepath : str) -> bool:
        result = os.path.exists(abs_filepath)
        if result: 
            print(f"{abs_filepath} already exists.")
        return result



    
    def get_card_source_code_directory(card_type : str, card_data_name : str):
        return rf"{global_source_code_output_directory}{card_type}s/source_code_{card_data_name}.html"

    def save_card_source_code(content:str, card_type : str, card_data_name : str) -> str:
        # Set output_directory
        output_directory = FileHandler.get_card_source_code_directory(card_type, card_data_name)
        
        return FileHandler.write_to_file_absolute_path(content, output_directory)
    
    def does_card_source_code_exist(card_type : str, card_data_name : str) -> str:
        # Set output_directory
        output_directory = FileHandler.get_card_source_code_directory(card_type, card_data_name)
        return FileHandler.__does_file_already_exist(output_directory)
    
    def read_card_source_code(card_type : str, card_data_name : str) -> str:
        output_directory = FileHandler.get_card_source_code_directory(card_type, card_data_name)
        return FileHandler.__read_file(output_directory)
    

    def get_card_pretty_code_directory(card_type : str, card_data_name : str) -> str:
        return rf"{global_source_code_output_directory}{card_type}s/Pretty/pretty_code_of_page_{card_data_name}.html"
    
    def save_card_pretty_code(content : str, card_type : str, card_data_name : str) -> str:
        # Set output_directory
        output_directory = FileHandler.get_card_pretty_code_directory(card_type, card_data_name)
        
        return FileHandler.write_to_file_absolute_path(content, output_directory)
    
    def does_card_pretty_code_exist(card_type : str, card_data_name : str) -> str:
        # Set output_directory
        output_directory = FileHandler.get_card_pretty_code_directory(card_type, card_data_name)
        return FileHandler.__does_file_already_exist(output_directory)



    def get_card_str_directory(card_type : str, card_data_name : str):
        return rf"{global_output_directory}{card_type}s/Strings/{card_data_name}.txt"

    
    def save_card_str(card_str : str, card_type : str, card_data_name : str) -> str:
        # Set output_directory
        output_directory = FileHandler.get_card_str_directory(card_type, card_data_name)
        
        return FileHandler.write_to_file_absolute_path(card_str, output_directory)
    
    def does_card_str_exist(card_type : str, card_data_name : str) -> str:
        # Set output_directory
        output_directory = FileHandler.get_card_str_directory(card_type, card_data_name)
        return FileHandler.__does_file_already_exist(output_directory)
    
    def read_card_str(card_type : str, card_data_name : str) -> str:
        output_directory = FileHandler.get_card_str_directory(card_type, card_data_name)

        return FileHandler.__read_file(output_directory)
    



    def get_card_list_source_code_directory(card_type : str, page_number : str):
        return rf"{global_list_output_directory}{card_type}s/source_code_of_page_{page_number}.html"
    
    def save_card_list_source_code(content:str, card_type : str, page_number : str) -> str:
        # Set output_directory
        output_directory = FileHandler.get_card_list_source_code_directory(card_type, page_number)
        
        return FileHandler.write_to_file_absolute_path(content, output_directory)
    
    def does_card_list_source_code_exist(card_type : str, page_number : str) -> str:
        # Set output_directory
        output_directory = FileHandler.get_card_list_source_code_directory(card_type, page_number)

        return FileHandler.__does_file_already_exist(output_directory)
    
    def read_card_list_source_code(card_type : str, page_number : str) -> str:
        output_directory = FileHandler.get_card_list_source_code_directory(card_type, page_number)

        return FileHandler.__read_file(output_directory)
        



    def get_card_list_pretty_code_directory(card_type : str, page_number : str):
        return rf"{global_list_output_directory}{card_type}s/Pretty/pretty_code_of_page_{page_number}.html"

    def save_card_list_pretty_code(content:str, card_type : str, page_number : str) -> str:
        # Set output_directory
        output_directory = FileHandler.get_card_list_pretty_code_directory(card_type, page_number)
        
        return FileHandler.write_to_file_absolute_path(content, output_directory)

    def does_card_list_pretty_code_exist(card_type : str, page_number : str) -> str:
        # Set output_directory
        output_directory = FileHandler.get_card_list_pretty_code_directory(card_type, page_number)

        return FileHandler.__does_file_already_exist(output_directory)
    



    

