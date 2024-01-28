import re
from data_forge.data_interpreters.context_interpreter import ContextInterpreter


class FeatInterpreter(ContextInterpreter):
    def __init__(self, source_code : str):
        super().__init__(source_code)
    
    def get_feat_synergy(self):
        return self._contains_element_with_atr('class', 'feat-synergy')

    def get_prerequisite(self):
        return self._extract_content('field--name-field-feat-prerequisite-formattd')

    def get_body(self):
        return self._extract_body('field--name-field-feat-details')

    def get_source(self):
        return self._extract_content('field--name-field-feat-source')