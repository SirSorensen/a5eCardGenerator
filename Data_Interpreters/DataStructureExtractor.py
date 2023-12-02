

from Data_Interpreters.CodeInterpreter import CodeInterpreter


class DataStructureExtractor(CodeInterpreter):
    def __init__(self, filepath : str):
        super().__init__(filepath)

    def extract_field_information(self, field_class : str = "", field_id : str = "") -> list[str]|str:
        if len(field_id) > 0:
            field_div = self.soup.find('div', id=field_id)
        else:
            field_div = self.soup.find('div', class_=field_class)
            
        if field_div:
            
            item_fields = field_div.find_all('div', class_='field--item')
            if item_fields:
                return CodeInterpreter.return_field_result([CodeInterpreter.get_text(item) for item in item_fields])
            
            # Concatenate the text within <p> tags while preserving line breaks
            paragraphs = field_div.find_all('p')
            if paragraphs:
                return CodeInterpreter.return_field_result(['\n'.join(CodeInterpreter.get_text(p) for p in paragraphs)])
            
            spans = field_div.find_all('span')
            if spans:
                return CodeInterpreter.return_field_result([CodeInterpreter.get_text(s) for s in spans])


            return CodeInterpreter.return_field_result([CodeInterpreter.get_text(field_div)])
        
        return ""  # Field not found in the HTML

    def extract_list_of_names(self) -> list[str]:
        field_td = self.soup.find_all('td', class_="views-field views-field-title")
            
        return CodeInterpreter.return_field_result([CodeInterpreter.get_text(item) for item in field_td])

    def extract_name(self) -> str:
        name = self.soup.find('title')

        if name:
            return CodeInterpreter.get_text(name).replace("| Level Up", "").strip()
        return ""

