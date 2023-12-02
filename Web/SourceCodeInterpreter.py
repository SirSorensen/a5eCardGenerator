
import re
from bs4 import BeautifulSoup


class CodeInterpreter:
    def __init__(self, html_code : str):
        self.html_code = html_code
        self.soup = BeautifulSoup(html_code, 'html.parser')

    def extract_single(self, input_str : str) -> str:
        soup_result_div = self.soup.find('div', class_=f'field--name-field-{input_str}')
    
        # If the result is a link, extract the text from the link
        soup_result_a = soup_result_div.find('a')


        if soup_result_a is not None:
            result = soup_result_a.text.strip()
        else:
            result = soup_result_div.text.strip()

        result = re.sub("\s\s+" , " ", result)
        return result

    def extract_multi(self, input_str : str) -> list[str]:
        soup_result_div = self.soup.find('div', class_=f'field--name-field-{input_str}')
        return [a.text.strip() if a else div.text.strip() for div in soup_result_div.find_all('div', class_='field--item')]


    def extract_field_information(self, field_name : str):
        field_div = self.soup.find('div', class_=f'field--name-{field_name}')
        
        if field_div:
            # Check if there are any <a> tags within the field_div
            a_tags = field_div.find_all('a')
            if a_tags:
                return [a.text.strip() for a in a_tags]
            
            item_fields = field_div.find_all('div', class_='field--item')
            if item_fields:
                return [item.text.strip() for item in item_fields]
            
            return [field_div.text.strip()]
        
        return None  # Field not found in the HTML