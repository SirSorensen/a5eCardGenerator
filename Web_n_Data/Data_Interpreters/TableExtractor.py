from Web_n_Data.Data_Interpreters.CodeInterpreter import CodeInterpreter


class TableExtractor(CodeInterpreter):
    def __init__(self, filepath : str):
        super().__init__(filepath)
        
    def extract_list_of_class(self, class_:str) -> list[str]|str:
        field_td = self.soup.find_all('td', class_=class_)

        result_texts = [CodeInterpreter.get_text(item) for item in field_td]
            
        return CodeInterpreter.try_unwrap_list(result_texts)

    def extract_list_of_class_with_link(self, class_:str):
        field_td = self.soup.find_all('td', class_=class_)

        results = [(CodeInterpreter.get_text(item), item.find('a')['href']) for item in field_td]
            
        return CodeInterpreter.try_unwrap_list(results)

    def is_next_page(self) -> bool:
        next_page_li = self.soup.find('li', class_="next")
        return next_page_li is not None