

import re
import time
import requests

from data_forge.data_structures.magic_item import MagicItem
from data_forge.data_structures.spell import Spell


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

def _get_sub_url(card_data_type : str):
    match card_data_type:
        case Spell.__name__:
            return r"spells?combine=&field_spell_ritual_value=All&page="
        case MagicItem.__name__:
            return r"magic-items?field_mi_cost_value%5Bmin%5D=&field_mi_cost_value%5Bmax%5D=&combine=&page="
        case _:
            raise ValueError(f"Card data type {card_data_type} is not supported by website_scraper.py")