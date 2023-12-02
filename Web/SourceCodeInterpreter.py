
import os
import re
from bs4 import BeautifulSoup, Comment


class CodeInterpreter:
    def __init__(self, file_path : str):
        self.file_path = file_path
        
        with open(file_path, "r", encoding='utf-8') as file:
            html_code = file.read()
            file.close()

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
        print(f"Prettifying {self.file_path}...")

        comments = self.soup.find_all(string=lambda text: isinstance(text, Comment))
        for comment in comments:
            comment.extract()

        filename_match = re.search(r'\w+\.\w+', self.file_path)

        if filename_match:
            filename = filename_match.group()
            file_path = self.file_path.replace(filename, 'Pretty\\' + filename.replace(".txt", ".html"))
            
            if not os.path.exists(file_path):
                os.makedirs(os.path.dirname(file_path), exist_ok=True)
                with open(file_path, "w") as f: pass


            with open(file_path, "w+", encoding='utf-8') as file:
                file.write(self.soup.prettify())
        else:
            print("No filename found in the file path.")


def return_field_result(field_result):
    field_result = strip_list(field_result)

    if len(field_result) == 1:
        return field_result[0]
    
    return field_result

def strip_list(list_to_strip : list):
    return [item.strip() for item in list_to_strip]

def get_text(item):
    return re.sub(r'\s{2,}', " ", item.get_text(separator=' ').strip())
