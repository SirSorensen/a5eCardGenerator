

import os

from FileHandler.FileHandler import write_to_file


def a5e_scrape_source_text(name : str, sub_url : str, output_folder : str = r'Outputs\\'):
    import requests

    name = str.lower(name)
    output_filepath = f"{output_folder}source_text_{name}.txt"

    url = f'https://a5e.tools/{sub_url}{name}'
    response = requests.get(url)
    response.raise_for_status()

    write_to_file(output_filepath, response.text)
    
    return response
