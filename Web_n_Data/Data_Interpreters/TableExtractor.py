import bs4
from Web_n_Data.Data_Interpreters.CodeInterpreter import CodeInterpreter

name_tag_class = "views-field views-field-title"
summary_tag_class = "views-field views-field-field-spell-summary"

# This class extracts data from the HTML of a table
class TableExtractor(CodeInterpreter):
    def __init__(self, filepath : str, page : int = 0, file_extension : str = ".html"):
        self.filepath = filepath
        self.page = page
        self.file_extension = file_extension
        abs_filepath = f"{filepath}{str(page)}{file_extension}"
        super().__init__(abs_filepath)

    # This function extracts a the contents of list tags from a source text 
    def __extract_list_of_class(self, class_:str) -> list[str]|str:
        field_td = self.soup.find_all('td', class_=class_)

        result_texts = [CodeInterpreter.get_text(item) for item in field_td]
            
        return CodeInterpreter.prettify_list(result_texts)

    # This function extracts a the contents of list tags and their hyper-links from a source text
    def __extract_list_of_class_with_link(self, class_:str):
        field_td = self.soup.find_all('td', class_=class_)

        results = [(CodeInterpreter.get_text(item), item.find('a')['href']) for item in field_td]
            
        return CodeInterpreter.prettify_list(results)

    # This function extracts the names their hyper-links of a table
    def extract_list_of_names_with_link(self):
        return self.__extract_list_of_class_with_link(name_tag_class)

    # This function extracts the summaries of a table
    def extract_list_of_summaries(self) -> list[str]|str:
        return self.__extract_list_of_class(summary_tag_class)

    # This function evaluates whether or not there is a next page
    def is_next_page(self) -> bool:
        next_page_li = self.soup.find('li', class_="next")
        return next_page_li is not None