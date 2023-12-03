

import re
import time
from Web_n_Data.File_Handlers.FileHandler import FileHandler
import requests


def a5e_scrape_source_text(name : str, sub_url : str, output_folder : str = "", web_url : str = "") -> str:
    name = str.lower(name)
    _name = name
    
    if web_url != "" and len(web_url) > 0:
        sub_url = str.lower(sub_url)
        sub_url += re.match(r'[\s\S]*\/', web_url).group()
        web_url = re.sub(r'[\w-]+(?=\/)', '', web_url)
        _name = web_url.replace("/", "")

    output_folder = r'Outputs\\' + output_folder
    output_filepath = f"{output_folder}source_text_{name}.txt"
    

    print(f"Scraping \'{_name}\' with sub-url \'{sub_url}\'...")

    url = f'https://a5e.tools/{sub_url}{_name}'
    response = requests.get(url)
    if response.status_code == 404:
        print(f"404: {url}")
    else:
        response.raise_for_status()

    FileHandler.write_to_file(output_filepath, response.text)

    time.sleep(3)
    
    return output_filepath
