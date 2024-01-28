import os
from data_forge.settings import *

global_output_directory = r"Outputs/"
global_html_output_directory = rf"{global_output_directory}HTML/"
global_source_code_output_directory = rf"{global_output_directory}Source_Code/"
global_list_output_directory = rf"{global_source_code_output_directory}Lists/"
global_slides_output_directory = rf"{global_output_directory}Slides/"
global_images_output_directory = rf"{global_output_directory}Images/"

class FileHandler:

    # Returns the contents of the file with file path = abs_filepath
    def read_file(abs_filepath : str) -> str:
        if os.path.exists(abs_filepath):
            with open(abs_filepath, "r", encoding='utf-8') as file:
                content = file.read()
                file.close()
            return content  
        
        else:
            raise ValueError(f"ERROR! File {abs_filepath} does not exist!")      

    # Returns the contents of the written file
    def write_to_file(content:str, output_abs_filepath:str):
        if debug: print(f"Writing to {output_abs_filepath}...")
        
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
            if debug: print(f"{abs_filepath} already exists.")
            return FileHandler.read_file(abs_filepath)


    def _make_file_if_not_exists(output_abs_filepath:str) -> str:
        if not os.path.exists(output_abs_filepath):
            os.makedirs(os.path.dirname(output_abs_filepath), exist_ok=True)
            with open(output_abs_filepath, "w") as f: pass
        return output_abs_filepath
    

    def does_file_exist(abs_filepath : str) -> bool:
        return os.path.exists(abs_filepath)
    

    def __gen_card_code_directory(card_type : str, context_name : str, code_type : str, file_extension : str = ".html"):
        return rf"{global_html_output_directory}{card_type}s/{code_type}/{context_name}{file_extension}"
    
    def __gen_source_code_directory(card_type : str, context_name : str, 
                                  is_table : bool = False, is_stripped : bool = False,
                                  is_str : bool = False, is_pretty : bool = False):
        code_type = None
        file_extension = ".html"
        if is_table:
            code_type = "Tables"
        elif is_str:
            code_type = "Strings"
            file_extension = ".txt"
        else:
            code_type = "Source_Code"
        
        if code_type is None:
            raise ValueError("ERROR! code_type is None!")
        

        if is_stripped:
            code_type += "/Stripped"

        if is_pretty:
            code_type += "/Pretty"
        
        return FileHandler.__gen_card_code_directory(card_type, context_name, code_type, file_extension)
        

    
    def gen_card_source_code_directory(card_type : str, context_name : str, is_pretty : bool = False):
        return FileHandler.__gen_source_code_directory(card_type, context_name, is_pretty=is_pretty)

    def gen_card_stripped_code_directory(card_type : str, context_name : str, is_pretty : bool = False):
        return FileHandler.__gen_source_code_directory(card_type, context_name, is_stripped=True, is_pretty=is_pretty)
    
    def gen_card_str_directory(card_type : str, context_name : str):
        return FileHandler.__gen_source_code_directory(card_type, context_name, is_str=True)

    def gen_card_list_source_code_directory(card_type : str, page_number : int, is_pretty : bool = False, is_stripped : bool = False):
        return FileHandler.__gen_source_code_directory(card_type, f"page_{str(page_number)}", is_table=True, is_pretty=is_pretty, is_stripped=is_stripped)
    
    def _get_global_output_directory():
        return global_output_directory
    
    def gen_slide_output_directory():
        return f"{global_slides_output_directory}{FileHandler.gen_slide_output_name()}"
    
    def gen_slide_output_name(file_extension : str = ".pptx"):
        return f"cardCreator-test{file_extension}"
    
    def gen_slide_img_output_path(sub_folder : str = ""):
        if sub_folder:
            sub_folder += "/"
        return f"{global_images_output_directory}{sub_folder}"
    
    def gen_slide_img_output_directory(sub_folder : str = ""):
        return f"{FileHandler.gen_slide_img_output_path(sub_folder)}{FileHandler.gen_slide_output_name('')}"
    
    def gen_project_abs_path():
        abs_project_path = os.path.abspath("main.py")
        abs_project_path = abs_project_path.replace("main.py", "")
        return abs_project_path

    

    

    