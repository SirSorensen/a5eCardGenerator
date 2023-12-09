import os
import re

class FileHandler:

    def write_to_file_absolute_path(content:str, output_abs_filepath:str, file_extension:str = "") -> str:
        output_abs_filepath = FileHandler.__gen_absolute_filepath(output_abs_filepath, file_extension)
        FileHandler.__write_to_file(output_abs_filepath, content)
        return output_abs_filepath
    
    def write_to_file_name(content:str, output_directory:str, output_name:str, file_extension:str = "") -> str:
        # If the name contains a sub-url, remove it and add it to the directory
        sub_url = re.match(r'[\s\S]*\/', output_name)
        if sub_url is not None:
            output_directory += sub_url.group()
            name = re.sub(r'[\w-]+(?=\/)', '', output_name)
            output_name = output_name.replace("/", "")
        
        # Lower the name
        output_name = str.lower(output_name)

        # Create the filepath
        output_abs_filepath = FileHandler.__gen_absolute_filepath(f"{output_directory}{output_name}", file_extension)

        FileHandler.__write_to_file(output_abs_filepath, content)

        return output_abs_filepath
        

    # Returns the absolute filepath
    def __write_to_file(output_abs_filepath:str, content:str):
        print(f"Writing to {output_abs_filepath}...")
        
        # Create the file if it doesn't exist
        FileHandler._make_file_if_not_exists(output_abs_filepath)
        
        # Write the content to the file
        with open(output_abs_filepath, "w+", encoding='utf-8') as file:
            file.write(content)

    def __gen_absolute_filepath(filepath:str, file_extension:str):
        filepath_extension = re.search(r'\.\w+$', filepath)

        # If the file extension is given, use it
        if file_extension != "":
            # If the file extension doesn't start with a dot, add it
            if file_extension[0] != ".":
                file_extension = "." + file_extension
            
            # Remove the file extension from the filepath if it exists
            if filepath_extension is not None:
                filepath = re.sub(r'\.\w+$', "", filepath)
         
        # Else, if the filepath has an extension, use it
        elif filepath_extension is not None:
            pass
        else:
            file_extension = ".txt"

        return f"{filepath}{file_extension}"

    def _make_file_if_not_exists(output_abs_filepath:str, file_extension:str = "") -> str:
        output_abs_filepath += file_extension
        if not os.path.exists(output_abs_filepath):
            os.makedirs(os.path.dirname(output_abs_filepath), exist_ok=True)
            with open(output_abs_filepath, "w") as f: pass
        return output_abs_filepath

    def read_file(abs_filepath):
        if os.path.exists(abs_filepath):
            with open(abs_filepath, "r", encoding='utf-8') as file:
                content = file.read()
                file.close()
        else:
            print(f"File not found: {abs_filepath}")
            content = ""

        return content
    
    def save_source_code(output_directory:str, output_name:str, content:str, file_extension:str = "") -> str:
        # If the output_folder does not end with "source_text_", add it
        if not output_directory.endswith("source_text_"):
            output_directory = f"{output_directory}source_text_"
        
        return FileHandler.save_output(output_directory, output_name, content, file_extension)
    
    def save_output(output_directory:str, output_name:str, content:str, file_extension:str = "") -> str:
        # If the output_directory does not start with "Outputs\", add it
        if not output_directory.startswith("Outputs\\"):
            output_directory = f"Outputs\\{output_directory}"

        return FileHandler.write_to_file_name(content, output_directory, output_name, file_extension)