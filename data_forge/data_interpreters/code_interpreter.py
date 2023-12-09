
import re
from bs4 import BeautifulSoup, Comment

from data_forge.file_handlers.file_handler import FileHandler




# CodeInterpreter is a class that interprets the code of a HTML file
class CodeInterpreter:
    def __init__(self, abs_filepath : str):
        # abs_filepath = The absolute path to the file to be interpreted
        self.abs_filepath = abs_filepath

        # html_code = The string of the contents of the file to be interpreted
        html_code = FileHandler.read_file(abs_filepath)

        # soup = The BeautifulSoup object of the file to be interpreted
        self.soup = BeautifulSoup(html_code, 'html.parser')



    # Prettify the html code and save it to a new file
    def prettify_html(self) -> str:
        print(f"Prettifying {self.abs_filepath}...")

        # Remove comments of the soup
        comments = self.soup.find_all(string=lambda text: isinstance(text, Comment))
        for comment in comments:
            comment.extract()

        # Prettify the soup by adding newlines and indents and remove extra whitespace in between tags    
        pretty_contents = self.soup.prettify()

        return pretty_contents



    # Strip list of strings and return it as a list of strings, unless there is only one string in the list, in which case return the string
    def prettify_list(list_to_prettify) -> list[str]|str:
        list_to_prettify = [item.strip() if isinstance(item, str) else item for item in list_to_prettify]

        if len(list_to_prettify) == 1:
            return list_to_prettify[0]
        
        return list_to_prettify


    # Return the text of an tag-item and replace the tags with a whitespace
    def get_text(item):
        return re.sub(r'\s{2,}', " ", item.get_text(separator=' ').strip())
