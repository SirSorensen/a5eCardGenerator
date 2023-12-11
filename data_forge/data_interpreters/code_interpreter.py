
import re
from bs4 import BeautifulSoup, Comment

# CodeInterpreter is a class that interprets the code of a HTML file
class CodeInterpreter:
    def __init__(self, source_code : str):
        # soup = The BeautifulSoup object of the contents to be interpreted
        self.soup = BeautifulSoup(source_code, 'html.parser')

    # Prettify the html code and save it to a new file
    def prettify_html(self) -> str:
        # Remove comments of the soup
        comments = self.soup.find_all(string=lambda text: isinstance(text, Comment))
        for comment in comments:
            comment.extract()

        # Prettify the soup by adding newlines and indents and remove extra whitespace in between tags    
        pretty_contents = self.soup.prettify()

        return pretty_contents
    
    # Prettify the html code and save it to a new file
    def prettify_html_source_code(source_code : str) -> str:
        soup = BeautifulSoup(source_code, 'html.parser')

        # Remove comments of the soup
        comments = soup.find_all(string=lambda text: isinstance(text, Comment))
        for comment in comments:
            comment.extract()

        # Prettify the soup by adding newlines and indents and remove extra whitespace in between tags    
        pretty_contents = soup.prettify()

        return pretty_contents
    
    def get_article_code(self) -> str:
        article = self.soup.find('article')
        return str(article)
    
    def prettify_article_code(self) -> str:
        article = self.soup.find('article')
        return CodeInterpreter.prettify_html_source_code(str(article))

    # Strip list of strings and return it as a list of strings, unless there is only one string in the list, in which case return the string
    def prettify_list(list_to_prettify):
        list_to_prettify = [item.strip() if isinstance(item, str) else item for item in list_to_prettify]

        if len(list_to_prettify) == 1:
            return list_to_prettify[0]
        
        return list_to_prettify

    # Return the text of an tag-item and replace the tags with a whitespace
    def get_text(item):
        return re.sub(r'\s{2,}', " ", item.get_text(separator=' ').strip())

    
    def __extract_item_fields(self, field) -> list[str]|str|None:
        item_fields = field.find_all('div', class_='field--item')
        if item_fields:
            return CodeInterpreter.prettify_list([CodeInterpreter.get_text(item) for item in item_fields])
        else:
            return None
    
    def __extract_paragraphs(self, field) -> list[str]|str|None:
        # Concatenate the text within <p> tags while preserving line breaks
        paragraphs = field.find_all('p')
        if paragraphs:
            return CodeInterpreter.prettify_list(['\n'.join(CodeInterpreter.get_text(p) for p in paragraphs)])
        else:  
            return None
    
    def __extract_spans(self, field) -> list[str]|str|None:
        spans = field.find_all('span')
        if spans:
            return CodeInterpreter.prettify_list([CodeInterpreter.get_text(s) for s in spans])
        else:
            return None
    
    # This function extracts a field's information from a Tag object
    def __extract_field_information(self, field) -> list[str]|str:
        if field:

            item_fields = self.__extract_item_fields(field)
            if item_fields: 
                return item_fields
            
            paragraphs = self.__extract_paragraphs(field)
            if paragraphs:
                return paragraphs

            spans = self.__extract_spans(field)
            if spans:
                return spans
            
            return CodeInterpreter.prettify_list([CodeInterpreter.get_text(field)])
            
        return ""  # Field not found in the HTML
    
    
    # This function extracts a div-tag's tag object from an id
    def extract_field_information_from_id(self, field_id : str) -> list[str]|str:
        field_div = self.soup.find('div', id=field_id)
        result = self.__extract_field_information(field_div)
        return result
    

    # This function extracts a div-tag's tag object from a class
    def extract_field_information_from_class(self, field_class : str) -> list[str]|str:
        field_div = self.soup.find('div', class_=field_class)      
        result = self.__extract_field_information(field_div)
        return result
    
    
    # This function extracts the title of a card from the HTML
    def extract_name(self) -> str:
        name = self.soup.find('title')

        if name:
            return CodeInterpreter.get_text(name).replace("| Level Up", "").strip()
        return ""
        