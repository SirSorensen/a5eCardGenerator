from bs4 import BeautifulSoup
from Web.CodeInterpreter import CodeInterpreter


class TableExtractor(CodeInterpreter):
    def __init__(self, filepath : str):
        super().__init__(filepath)
        
    def extract_list_of_names(self) -> list[str]:
        field_td = self.soup.find_all('td', class_="views-field views-field-title")


        result_texts = [CodeInterpreter.get_text(item) for item in field_td]
            
        return CodeInterpreter.return_field_result(result_texts)

    def is_next_page(self) -> (bool, str):
        next_page_li = self.soup.find('li', class_="next")
        if next_page_li:
            next_page_a = next_page_li.find('a')
            if next_page_a:
                return True, next_page_a['href']
        
        return (False, "")