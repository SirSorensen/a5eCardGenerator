
import re
from bs4 import BeautifulSoup, Comment

from Web_n_Data.File_Handlers.FileHandler import read_file, write_to_file


class CodeInterpreter:
    def __init__(self, filepath : str):
        self.filepath = filepath

        html_code = read_file(filepath)

        self.soup = BeautifulSoup(html_code, 'html.parser')

    def prettify_soup(self):
        print(f"Prettifying {self.filepath}...")

        comments = self.soup.find_all(string=lambda text: isinstance(text, Comment))
        for comment in comments:
            comment.extract()

        filename = re.search(r'[^\\]+\.\w+', self.filepath).group()
        filepath = self.filepath.replace(filename, 'Pretty\\' + filename.replace(".txt", ".html"))
            
        write_to_file(filepath, self.soup.prettify())


    def try_unwrap_list(field_result) -> list[str]|str:
        field_result = CodeInterpreter.strip_list(field_result)

        if len(field_result) == 1:
            return field_result[0]
        
        return field_result

    def strip_list(list_to_strip : list):
        return [item.strip() if isinstance(item, str) else item for item in list_to_strip]

    def get_text(item):
        return re.sub(r'\s{2,}', " ", item.get_text(separator=' ').strip())
