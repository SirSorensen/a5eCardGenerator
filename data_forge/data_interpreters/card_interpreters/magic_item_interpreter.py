import re
from data_forge.data_interpreters.context_interpreter import ContextInterpreter


class MagicItemInterpreter(ContextInterpreter):
    def __init__(self, source_code : str):
        super().__init__(source_code)

    def get_category(self):
        category_rarity_cost_str = self._extract_content('magic-item-category-rarity-cost')
        category_str = re.search(r'[\s\w]*[^\,](?=\,)', category_rarity_cost_str).group()
        return category_str.rstrip()
    
    def get_rarity(self):
        rarity_str = self._extract_content('magic-item-rarity', tag_type='span')
        return rarity_str
    
    def get_cost(self) -> int:
        cost_str = self._extract_content('magic-item-cost-number', tag_type='span', atr_name='id')
        cost_int = int(cost_str)
        return cost_int
    
    def get_crafting_components(self):
        return self._extract_content('field--name-field-mi-crafting-components')
    
    def get_body(self):
        return self._extract_body('field--name-field-mi-description')
    
    def get_source(self):
        return self._extract_content('field--name-field-mi-source')