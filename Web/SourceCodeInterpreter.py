
import re
from bs4 import BeautifulSoup


class CodeInterpreter:
    def __init__(self, html_code : str):
        self.html_code = html_code
        self.soup = BeautifulSoup(html_code, 'html.parser')



    def extract_field_information(self, field_class : str = "", field_id : str = "") -> list[str]|str:
        if len(field_id) > 0:
            field_div = self.soup.find('div', id=field_id)
                    
            if field_div:  
                item_fields = field_div.find_all('div', class_='field--item')
                if item_fields:
                    return return_field_result([item.get_text(separator=' ') for item in item_fields])
                
                # Concatenate the text within <p> tags while preserving line breaks
                paragraphs = field_div.find_all('p')
                if paragraphs:
                    return return_field_result(['\n'.join(re.sub(r'\s{2,}', " ", p.get_text(separator=' ').strip()) for p in paragraphs)])


                return return_field_result([field_div.get_text(separator=' ')])
            
            return [""]  # Field not found in the HTML
        else:
            field_div = self.soup.find('div', class_=field_class)
            
            if field_div:
                
                item_fields = field_div.find_all('div', class_='field--item')
                if item_fields:
                    return return_field_result([item.get_text(separator=' ') for item in item_fields])
                
                # Concatenate the text within <p> tags while preserving line breaks
                paragraphs = field_div.find_all('p')
                if paragraphs:
                    return return_field_result(['\n'.join(re.sub(r'\s{2,}', " ", p.get_text(separator=' ').strip()) for p in paragraphs)])


                return return_field_result([field_div.get_text(separator=' ')])
            
            return [""]  # Field not found in the HTML


def return_field_result(field_result):
    field_result = strip_list(field_result)

    if len(field_result) == 1:
        return field_result[0]
    
    return field_result

def strip_list(list_to_strip : list):
    return [item.strip() for item in list_to_strip]

