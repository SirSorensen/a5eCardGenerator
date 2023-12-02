
import re
from bs4 import BeautifulSoup


class CodeInterpreter:
    def __init__(self, html_code : str):
        self.html_code = html_code
        self.soup = BeautifulSoup(html_code, 'html.parser')

    def extract_field_information(self, field_name : str) -> list[str]|str:
        field_div = self.soup.find('div', class_=f'field--name-{field_name}')
        
        if field_div:
            # Check if there are any <a> tags within the field_div
            a_tags = field_div.find_all('a')
            if a_tags:
                return return_field_result([a.text for a in a_tags])
            
            p_tags = field_div.find_all('p')
            if p_tags:
                return return_field_result([p.text for p in p_tags])
            
            item_fields = field_div.find_all('div', class_='field--item')
            if item_fields:
                return return_field_result([item.text for item in item_fields])
            
            return return_field_result([field_div.text])
        
        return ""  # Field not found in the HTML






def return_field_result(field_result):
    field_result = strip_list(field_result)

    if len(field_result) == 1:
        return field_result[0]
    
    return field_result

def strip_list(list_to_strip : list):
    return [re.sub("\s\s+" , " ", item).strip() for item in list_to_strip]