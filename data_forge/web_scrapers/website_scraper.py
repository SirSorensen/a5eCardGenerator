

import re
import time
import requests


def scrape_source_text(url_ending : str, sub_url : str = "") -> str:

    # If the url_ending contains a sub-url, remove it and add it to the sub_url
    url_ending_head_match = re.match(r'[\s\S]*\/', url_ending)
    if url_ending_head_match is not None:
        web_url_head = url_ending_head_match.group()
        sub_url += web_url_head
        url_ending = url_ending.replace(web_url_head, "")
    
    url = f'https://a5e.tools/{sub_url}{url_ending}'

    print(f"Scraping \'{url_ending}\' with url \'{url}\'...")

    response = requests.get(url)
    if response.status_code == 404:
        print(f"404: {url}")
    else:
        response.raise_for_status()

    time.sleep(3)
    
    return response.text