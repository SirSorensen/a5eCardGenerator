import os

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
            print(f"{abs_filepath} already exists.")
            return FileHandler.read_file(abs_filepath)


    def _make_file_if_not_exists(output_abs_filepath:str) -> str:
        if not os.path.exists(output_abs_filepath):
            os.makedirs(os.path.dirname(output_abs_filepath), exist_ok=True)
            with open(output_abs_filepath, "w") as f: pass
        return output_abs_filepath
    

    def does_file_exist(abs_filepath : str) -> bool:
        return os.path.exists(abs_filepath)

    
    def gen_card_source_code_directory(card_type : str, context_name : str):
        return rf"{global_source_code_output_directory}{card_type}s/{context_name}.html"

    def gen_card_article_code_directory(card_type : str, context_name : str):
        return rf"{global_source_code_output_directory}{card_type}s/Article/{context_name}.html"

    def gen_card_pretty_code_directory(card_type : str, context_name : str) -> str:
        return rf"{global_source_code_output_directory}{card_type}s/Pretty/page_{context_name}.html"
    
    def gen_card_str_directory(card_type : str, context_name : str):
        return rf"{global_output_directory}Strings/{card_type}s/{context_name}.txt"

    def gen_card_list_source_code_directory(card_type : str, page_number : str):
        return rf"{global_list_output_directory}{card_type}s/page_{page_number}.html"

    def gen_card_list_pretty_code_directory(card_type : str, page_number : str):
        return rf"{global_list_output_directory}{card_type}s/Pretty/{page_number}.html"
    
    def _get_global_output_directory():
        return global_output_directory


    
    def old_gen_card_source_code_directory(card_type : str, context_name : str):
        return rf"{global_source_code_output_directory}{card_type}s/source_code_{context_name}.html"
    

    def old_gen_card_pretty_code_directory(card_type : str, context_name : str) -> str:
        return rf"{global_source_code_output_directory}{card_type}s/Pretty/pretty_code_of_page_{context_name}.html"

    def old_gen_card_list_source_code_directory(card_type : str, page_number : str):
        return rf"{global_list_output_directory}{card_type}s/source_code_of_page_{page_number}.html"

    def old_gen_card_list_pretty_code_directory(card_type : str, page_number : str):
        return rf"{global_list_output_directory}{card_type}s/Pretty/pretty_code_of_page_{page_number}.html"
    
    def rename_old_files():
        for dirpath, dirnames, filenames in os.walk(FileHandler._get_global_output_directory()):
            for name in filenames:
                abs_filepath = os.path.join(dirpath, name)
                new_abs_filepath = abs_filepath              
                if name.startswith("source_code_of_"):
                    new_abs_filepath = os.path.join(dirpath, name.replace("source_code_of_", ""))
                elif name.startswith("source_code_"):
                    new_abs_filepath = os.path.join(dirpath, name.replace("source_code_", ""))
                elif name.startswith("pretty_code_of_"):
                    new_abs_filepath = os.path.join(dirpath, name.replace("pretty_code_of_", ""))
                elif name.startswith("pretty_code_"):
                    new_abs_filepath = os.path.join(dirpath, name.replace("pretty_code_", ""))
                elif name.startswith("page_") and '/Lists/' not in abs_filepath:
                    new_abs_filepath = os.path.join(dirpath, name.replace("page_", ""))
                
                if not FileHandler.does_file_exist(new_abs_filepath):
                    os.rename(abs_filepath, new_abs_filepath)
                elif new_abs_filepath != abs_filepath:
                    os.remove(abs_filepath)
                    print(f"Removed {abs_filepath} because {new_abs_filepath} already exists.")