
from data_forge.data_structures.combat_maneuver import CombatManeuver
from data_forge.data_structures.magic_item import MagicItem
from data_forge.data_structures.monster import Monster
from data_forge.data_structures.spell import Spell
from data_forge.data_structures.feat import Feat
import time
import requests

# Scrapes the source text of a given website. 
# Inputs: For example in https://a5e.tools/spell/aid, url_ending = 'spell/aid' and url_start = 'https://a5e.tools/'
# Returns the contents of the scraped website.
def scrape_source_code(url_ending : str, url_start : str = "https://a5e.tools/") -> str:
    
    url = rf'{url_start}{url_ending}'

    print(f"Scraping \'{url}\'...")

    response = requests.get(url)
    if response.status_code == 404:
        print(f"404: {url}")
    else:
        response.raise_for_status()

    time.sleep(10)
    
    return response.text


# Scrapes the source text of a table with the given parge number and card type
# Returns the contents of the scraped table's website.
def scrape_table_source_code(card_type : str, page_number : int = 0) -> str:
    # Generate the url ending of the table
    url_ending = __get_table_url_ending(card_type, page_number)
    # Scrape the source text
    source_text = scrape_source_code(url_ending)
    return source_text

# Generates the url ending for a table of a given card type.
# Returns the generated url ending
def __get_table_url_ending(card_type : str, page_number):
    match card_type:
        case Spell.__name__:
            return r"spells?combine=&field_spell_ritual_value=All&page=" + str(page_number)
        case MagicItem.__name__:
            return r"magic-items?field_mi_cost_value%5Bmin%5D=&field_mi_cost_value%5Bmax%5D=&combine=&page=" + str(page_number)
        case CombatManeuver.__name__:
            return r"combat-maneuvers?combine=&page=" + str(page_number)
        case Feat.__name__:
            return r"feats"
        case Monster.__name__:
            return r"monsters?combine=&page=" + str(page_number)
        case _:
            raise ValueError(f"Card data type {card_type} is not supported by TableScraper.py")