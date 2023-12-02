from bs4 import BeautifulSoup
from Data_Interpreters.CodeInterpreter import CodeInterpreter


class TableExtractor(CodeInterpreter):
    def __init__(self, filepath : str):
        super().__init__(filepath)
        
    def extract_list_of_names(self) -> list[str]:
        field_td = self.soup.find_all('td', class_="views-field views-field-title")

        result_texts = [CodeInterpreter.get_text(item) for item in field_td]
            
        return CodeInterpreter.return_field_result(result_texts)

    def is_next_page(self) -> bool:
        next_page_li = self.soup.find('li', class_="next")
        return next_page_li is not None