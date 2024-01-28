from data_forge.settings import *
import re
from bs4 import BeautifulSoup, Comment, PageElement, Tag

# CodeInterpreter is a class that interprets the code of a HTML file
class CodeInterpreter:
    def __init__(self, source_code : str, stripped_tag : str):
        # soup = The BeautifulSoup object of the contents to be interpreted
        self.soup = BeautifulSoup(source_code, 'html.parser')
        self._stripped_soup = self.soup.find(stripped_tag)


    # Strip list of strings and return it as a list of strings
    def prettify_list(list_to_prettify):
        list_to_prettify = [CodeInterpreter.get_text(element) for element in list_to_prettify]

        list_to_prettify = [item.strip() if isinstance(item, str) else item for item in list_to_prettify]

        if len(list_to_prettify) == 1:
            return list_to_prettify[0]
        
        return list_to_prettify

    # Return the text of an element and replace the tags with a whitespace
    def get_text(element : PageElement):
        return re.sub(r'\s{2,}', " ", element.get_text(separator=' ').strip())    


    # -------------------------------------------------------- Prettifying Functions: -------------------------------------------------------- #


    # Return a prettified version of the given html code
    def _prettify_soup(soup : BeautifulSoup) -> str:
        # Remove comments of the soup
        soup = CodeInterpreter._remove_comments(soup)

        # Prettify the soup
        pretty_contents = soup.prettify()

        return pretty_contents

    def _remove_comments(soup : BeautifulSoup) -> BeautifulSoup:
        comments : list[PageElement] = soup.find_all(string=lambda text: isinstance(text, Comment))
        for comment in comments:
            comment.extract()
        return soup
    
    # Prettify the html code and save it to a new file
    def get_pretty_code(self) -> str:
        return CodeInterpreter._prettify_soup(self.soup)
    
    # Stripped code is the code of the article or table, ignoring all menu bars and other irrelevant information.
    def get_stripped_code(self) -> str:
        return str(self._stripped_soup)
    
    def get_pretty_stripped_code(self) -> str:
        return CodeInterpreter._prettify_soup(self._stripped_soup)