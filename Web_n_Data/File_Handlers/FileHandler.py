

import os


def write_to_file(filepath:str, content:str):
    # Create the file if it doesn't exist
    make_file_if_not_exists(filepath)
    
    # Write the content to the file
    with open(filepath, "w+", encoding='utf-8') as file:
        file.write(content)

def make_file_if_not_exists(filepath:str):
    if not os.path.exists(filepath):
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, "w") as f: pass

def read_file(filepath):
    with open(filepath, "r", encoding='utf-8') as file:
        content = file.read()
        file.close()
    
    return content