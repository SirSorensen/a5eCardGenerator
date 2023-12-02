
import os
import re
from bs4 import BeautifulSoup, Comment

from FileHandler.FileHandler import read_file, write_to_file


class CodeInterpreter:
    def __init__(self, filepath : str):
        self.filepath = filepath

        html_code = read_file(filepath)

        self.soup = BeautifulSoup(html_code, 'html.parser')


    def extract_field_information(self, field_class : str = "", field_id : str = "") -> list[str]|str:
        if len(field_id) > 0:
            field_div = self.soup.find('div', id=field_id)
        else:
            field_div = self.soup.find('div', class_=field_class)
            
        if field_div:
            
            item_fields = field_div.find_all('div', class_='field--item')
            if item_fields:
                return return_field_result([get_text(item) for item in item_fields])
            
            # Concatenate the text within <p> tags while preserving line breaks
            paragraphs = field_div.find_all('p')
            if paragraphs:
                return return_field_result(['\n'.join(get_text(p) for p in paragraphs)])
            
            spans = field_div.find_all('span')
            if spans:
                return return_field_result([get_text(s) for s in spans])


            return return_field_result([get_text(field_div)])
        
        return ""  # Field not found in the HTML

    def extract_name(self) -> str:
        name = self.soup.find('title')

        if name:
            return get_text(name).replace("| Level Up", "").strip()
        return ""

    def prettify_soup(self):
        print(f"Prettifying {self.filepath}...")

        comments = self.soup.find_all(string=lambda text: isinstance(text, Comment))
        for comment in comments:
            comment.extract()

        filename = re.search(r'[^\\]+\.\w+', self.filepath).group()
        filepath = self.filepath.replace(filename, 'Pretty\\' + filename.replace(".txt", ".html"))
            
        write_to_file(filepath, self.soup.prettify())


def return_field_result(field_result):
    field_result = strip_list(field_result)

    if len(field_result) == 1:
        return field_result[0]
    
    return field_result

def strip_list(list_to_strip : list):
    return [item.strip() for item in list_to_strip]

def get_text(item):
    return re.sub(r'\s{2,}', " ", item.get_text(separator=' ').strip())
