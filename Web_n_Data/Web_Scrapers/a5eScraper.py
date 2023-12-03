

import re
import time
from Web_n_Data.File_Handlers.FileHandler import FileHandler
import requests


def a5e_scrape_source_text(name : str, output_directory : str, url_ending : str = "", sub_url : str = "") -> str:

    # If no url_ending is provided, use the name as the url_ending
    if url_ending == "":
        url_ending = name

    # If the url_ending contains a sub-url, remove it and add it to the sub_url
    url_ending_head_match = re.match(r'[\s\S]*\/', url_ending)
    if url_ending_head_match is not None:
        web_url_head = url_ending_head_match.group()
        sub_url += web_url_head
        url_ending = url_ending.replace(web_url_head, "")

    # If the output_directory does not start with "Outputs\", add it
    if not output_directory.startswith("Outputs\\"):
        output_directory = f"Outputs\\{output_directory}"
    # If the output_folder does not end with "source_text_", add it
    if not output_directory.endswith("source_text_"):
        output_directory = f"{output_directory}source_text_"
    
    url = f'https://a5e.tools/{sub_url}{url_ending}'

    print(f"Scraping \'{url_ending}\' with url \'{url}\'...")

    response = requests.get(url)
    if response.status_code == 404:
        print(f"404: {url}")
    else:
        response.raise_for_status()

    output_abs_filepath = FileHandler.write_to_file_name(response.text, output_directory, name, ".html")

    time.sleep(3)
    
    return output_abs_filepath
