
import os
from data_forge.file_handlers.file_handler import FileHandler

root = FileHandler._get_global_output_directory()

class FileCleaner(FileHandler):


    def move_old_files():
        for dirpath, dirnames, filenames in os.walk(root):
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
                        code_type = "Tables"
                    case l if "Source_Code" in l:
                        code_type = "Source_Code"
                    case l if "Pickled" in l:
                        pass
                    case _:
                        print(f"ERROR! Could not determine code_type for {abs_filepath}.")

                if code_type:
                    if "Stripped" in dirpath or "Article" in dirpath:
                        code_type += "/Stripped"

                    if "Pretty" in dirpath:
                        code_type += "/Pretty"

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



    # Rename all files with legacy naming
    # Update as you go
    def rename_old_files():
        for dirpath, dirnames, filenames in os.walk(root):
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
    

    # Delete all files that are not source code or tables
    def clean_generated_files():
        for dirpath, dirnames, filenames in os.walk(root):
            for name in filenames:

                if not (dirpath.endswith("Source_Code") or dirpath.endswith("Tables")):
                    abs_filepath = os.path.join(dirpath, name)
                    os.remove(abs_filepath)
                    print(f"Removed {abs_filepath}.")


    
