import os
import re

global_output_directory = r"Outputs/"
global_html_output_directory = rf"{global_output_directory}HTML/"
global_source_code_output_directory = rf"{global_output_directory}Source_Code/"
global_list_output_directory = rf"{global_source_code_output_directory}Lists/"

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
            print(f"{abs_filepath} already exists.")
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
                                  is_table : bool = False, is_article : bool = False,
                                  is_str : bool = False, is_pretty : bool = False):
        code_type = None
        file_extension = ".html"
        if is_table:
                code_type = "Tables"
        elif is_article:
                code_type = "Articles"
        elif is_str:
                code_type = "Strings"
                file_extension = ".txt"
        else:
                code_type = "Source_Code"

        if code_type is None:
            raise ValueError("ERROR! code_type is None!")

        if is_pretty:
            code_type += "/Pretty"
        
        return FileHandler.__gen_card_code_directory(card_type, context_name, code_type, file_extension)
        

    
    def gen_card_source_code_directory(card_type : str, context_name : str, is_pretty : bool = False):
        return FileHandler.__gen_source_code_directory(card_type, context_name, is_pretty=is_pretty)

    def gen_card_article_code_directory(card_type : str, context_name : str, is_pretty : bool = False):
        return FileHandler.__gen_source_code_directory(card_type, context_name, is_article=True, is_pretty=is_pretty)
    
    def gen_card_str_directory(card_type : str, context_name : str):
        return FileHandler.__gen_source_code_directory(card_type, context_name, is_str=True)

    def gen_card_list_source_code_directory(card_type : str, page_number : int, is_pretty : bool = False):
        return FileHandler.__gen_source_code_directory(card_type, f"page_{str(page_number)}", is_table=True, is_pretty=is_pretty)
    
    def _get_global_output_directory():
        return global_output_directory
    

    

    def move_old_files():
        for dirpath, dirnames, filenames in os.walk(FileHandler._get_global_output_directory()):
            for name in filenames:
                abs_filepath = os.path.join(dirpath, name)
                
                # Determine card type
                card_type = None
                match dirpath:
                    case l if "CombatManeuvers" in l:
                        card_type = "CombatManeuver"
                    case l if "MagicItems" in l:
                        card_type = "MagicItem"
                    case l if "Monsters" in l:
                        card_type = "Monster"
                    case l if "Spells" in l:
                        card_type = "Spell"
                    case l if "Feats" in l:
                        card_type = "Feat"
                
                # Determine code type (Source_Code or Lists and Pretty or not)
                code_type = None
                match dirpath:
                    case l if "Lists" in l or "Tables" in l:
                        if "Pretty" in l:
                            code_type = "Tables/Pretty"
                        else:
                            code_type = "Tables"
                    case l if "Source_Code" in l:
                        if "Pretty" in l:
                            code_type = "Source_Code/Pretty"
                        else:
                            code_type = "Source_Code"

                # Card type and code type are both known, so we can move the file
                if card_type and code_type:
                    new_abs_filepath = FileHandler.__gen_card_code_directory(card_type, name.replace(".html", ""), code_type)
                    
                    # If the file doesn't exist yet, move it
                    if not FileHandler.does_file_exist(new_abs_filepath):
                        os.makedirs(os.path.dirname(new_abs_filepath), exist_ok=True)
                        os.rename(abs_filepath, new_abs_filepath)
                    
                    # If the file already exists, remove the old file
                    elif new_abs_filepath != abs_filepath:
                        print(f"Removed {abs_filepath} because {new_abs_filepath} already exists.")
                        os.remove(abs_filepath)
                else:
                    print(f"ERROR! Could not determine card_type or code_type for {abs_filepath}.")
                    print(f"card_type: {card_type}")
                    print(f"code_type: {code_type}")


    def rename_old_files():
        for dirpath, dirnames, filenames in os.walk(FileHandler._get_global_output_directory()):
            for name in filenames:
                abs_filepath = os.path.join(dirpath, name)

                new_abs_filepath = abs_filepath   

                # Determine replacement string for renaming the file (if any)
                replace_str = None 
                match name:
                    case s if s.startswith("source_code_of_"):
                        replace_str = "source_code_of_"
                    case s if s.startswith("source_code_"):
                        replace_str = "source_code_"
                    case s if s.startswith("pretty_code_of_"):
                        replace_str = "pretty_code_of_"
                    case s if s.startswith("pretty_code_"):
                        replace_str = "pretty_code_"
                    case s if not s.startswith("page_") and "\\Lists\\" in abs_filepath:
                        new_abs_filepath = os.path.join(dirpath, "page_" + name)
                    case s if s.startswith("page_") and not ("\\Lists\\" in abs_filepath):
                        replace_str = "page_"

                # Set new_abs_filepath if replace_str was determined    
                if replace_str:
                    new_abs_filepath = os.path.join(dirpath, name.replace(replace_str, ""))
                
                # Rename the file if it doesn't exist yet
                if not FileHandler.does_file_exist(new_abs_filepath):
                    os.rename(abs_filepath, new_abs_filepath)
                elif new_abs_filepath != abs_filepath:
                    os.remove(abs_filepath)
                    print(f"Removed {abs_filepath} because {new_abs_filepath} already exists.")