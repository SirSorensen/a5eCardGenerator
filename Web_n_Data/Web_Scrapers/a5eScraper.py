

import re
import time
from Web_n_Data.File_Handlers.FileHandler import write_to_file
import requests


def a5e_scrape_source_text(name : str, sub_url : str, output_folder : str = "") -> str:

    output_folder = r'Web_n_Data\\Outputs\\' + output_folder

    name = str.lower(name)
    if len(name) > 0:
        sub_url += re.match(r'[\s\S]*\/', name).group()
        name = re.sub(r'[\w-]+(?=\/)', '', name)
        name = name.replace("/", "")

    output_filepath = f"{output_folder}source_text_{name}.txt"
    
    print(f"Scraping \'{name}\' with sub-url \'{sub_url}\'...")

    url = f'https://a5e.tools/{sub_url}{name}'
    response = requests.get(url)
    if response.status_code == 404:
        print(f"404: {url}")
    else:
        response.raise_for_status()

    write_to_file(output_filepath, response.text)

    time.sleep(3)
    
    return output_filepath
