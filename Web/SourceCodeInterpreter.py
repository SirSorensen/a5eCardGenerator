
import re
from bs4 import BeautifulSoup


class CodeInterpreter:
    def __init__(self, html_code : str):
        self.html_code = html_code
        self.soup = BeautifulSoup(html_code, from_encoding='utf-8')



    def extract_field_information(self, field_name : str) -> list[str]|str:
        field_div = self.soup.find('div', class_=f'field--name-{field_name}')
        
        if field_div:
            
            item_fields = field_div.find_all('div', class_='field--item')
            if item_fields:
                return return_field_result([item.get_text(separator=' ') for item in item_fields])
            
            return return_field_result([field_div.get_text(separator=' ')])
        
        return ""  # Field not found in the HTML


def return_field_result(field_result):
    field_result = strip_list(field_result)

    if len(field_result) == 1:
        return field_result[0]
    
    return field_result

def strip_list(list_to_strip : list):
    return [re.sub("\s\s+" , " ", item).strip() for item in list_to_strip]

