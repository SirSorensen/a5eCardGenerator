
import re
from bs4 import BeautifulSoup, Comment, NavigableString, PageElement, ResultSet, Tag
from data_forge.data_interpreters.code_interpreter import CodeInterpreter
from data_forge.data_structures.context_contents import Paragraph, Paragraphs

class ContextInterpreter(CodeInterpreter):
    def __init__(self, source_code : str):
        super().__init__(source_code, 'article')


    def __get_contents(element : PageElement) -> str:
        if element is None:
            return ""
        
        element_text = element.get_text(separator=' ', strip=True)
        stripped_element_text = element_text.rstrip()
        return stripped_element_text


    def _extract_content_list(self, atr_val : str, tag_type : str = 'div', atr_name : str = 'class') -> list[str]:
        found_element = self._stripped_soup.find(tag_type, attrs={atr_name : atr_val})
        return ContextInterpreter._extract_field_items(found_element)
    
    def _extract_field_items(element : Tag) -> list:
        if element is None:
            return []
        
        field_items = element.find_all('div', class_='field--item')
        field_items_contents = [ContextInterpreter.__get_contents(item) for item in field_items]
        return field_items_contents
    
    def _extract_content(self, atr_val : str, tag_type : str = 'div', atr_name : str = 'class') -> str:
        found_element = self._stripped_soup.find(tag_type, attrs={atr_name : atr_val})

        if found_element is None:
            return ""
        
        element_classes = found_element.get('class')

        if element_classes and ('field--label-above' in element_classes or 'field--label-inline' in element_classes):
            element_str_list = self._extract_content_list(atr_val, atr_name=atr_name)
            if len(element_str_list) > 1:
                raise ValueError(f"Multiple found for {atr_name} \'{atr_val}\'")
            element_str = element_str_list[0]
        else:
            element_str = ContextInterpreter.__get_contents(found_element)


        return element_str
    
    def _content_to_int(element_str : str, default_val : int = -1, regex_pattern : str = ''):
        if element_str == "":
            return default_val
        
        if regex_pattern == "":
            return int(element_str)
        
        element_match = re.search(regex_pattern, element_str)

        if element_match is None:
            raise ValueError(f"Could not find regex pattern \'{regex_pattern}\' in \'{element_str}\'")
        
        return int(element_match.group())
    
    def _contains_element_with_atr(self, atr_name : str, atr_val : str) -> bool:
        return self._stripped_soup.find('a', attrs={atr_name : atr_val}) is not None

    def _extract_body(self, class_attribute : str) -> Paragraphs:
        # Extract the element containing the context
        context_element = self.soup.find('div', class_=class_attribute)
        if context_element is None:
            return None

        # Remove comments from the context element
        context_element : BeautifulSoup = CodeInterpreter._remove_comments(context_element)
        
        # Extract the paragraphs within the context element
        context_paragraphs : ResultSet[Tag] = context_element.find_all('p')
        if not context_paragraphs:
            return None

        result = Paragraphs()
        for context_paragraph in context_paragraphs:
            paragraph = ContextInterpreter.__extract_paragraph(context_paragraph)
            result.add_paragraph(paragraph)
        
        return result
    

    # This function extracts the contents of a tag object and returns it as a Paragraph object
    def __extract_paragraph(element : PageElement, acc : Paragraph = None) -> Paragraph:
        if acc is None:
            acc = Paragraph()

        for content in element.contents:
            if isinstance(content, NavigableString):
                # Direct text content
                acc.add_text(content.rstrip())
            
            elif isinstance(content, Tag) and content.name == 'a':
                # Link with text and href
                text = content.get_text(strip=True)
                href = content.get('href')
                acc.add_link(text, href)

            elif isinstance(content, Tag) and content.name == 'strong':
                # Title text
                text = content.get_text(strip=True)
                acc.add_title_text(text)

            elif isinstance(content, Tag):
                # Recursively extract contents
                acc = ContextInterpreter.__extract_paragraph(content, acc)
        
        return acc
            
            

        
