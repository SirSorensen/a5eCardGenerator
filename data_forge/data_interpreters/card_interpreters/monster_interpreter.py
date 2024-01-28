import re
from data_forge.data_interpreters.context_interpreter import ContextInterpreter


class MonsterInterpreter(ContextInterpreter):
    def __init__(self, source_code : str):
        super().__init__(source_code)

    def get_size(self):
        return self._extract_content('field--name-field-monster-size')
    
    def get_type(self):
        return self._extract_content('field--name-field-monster-type')
    
    def get_challenge_rating(self) -> int:
        cr_str = self._extract_content('field--name-field-monster-challenge-rating')
        cr_int = ContextInterpreter._content_to_int(cr_str, regex_pattern=r'\d+')
        return cr_int
    
    def get_terrain(self):
        return self._extract_content_list('field--name-field-monster-terrain')
    
    def get_strength_val(self):
        strength_str = self._extract_content('str-value', atr_name='id')
        strength_int = ContextInterpreter._content_to_int(strength_str, regex_pattern=r'\d+')
        return strength_int

    def get_dexterity_val(self):
        dexterity_str = self._extract_content('dex-value', atr_name='id')
        dexterity_int = ContextInterpreter._content_to_int(dexterity_str, regex_pattern=r'\d+')
        return dexterity_int
    
    def get_constitution_val(self):
        constitution_str = self._extract_content('con-value', atr_name='id')
        constitution_int = ContextInterpreter._content_to_int(constitution_str, regex_pattern=r'\d+')
        return constitution_int
    
    def get_intelligence_val(self):
        intelligence_str = self._extract_content('int-value', atr_name='id')
        intelligence_int = ContextInterpreter._content_to_int(intelligence_str, regex_pattern=r'\d+')
        return intelligence_int
    
    def get_wisdom_val(self):
        wisdom_str = self._extract_content('wis-value', atr_name='id')
        wisdom_int = ContextInterpreter._content_to_int(wisdom_str, regex_pattern=r'\d+')
        return wisdom_int
    
    def get_charisma_val(self):
        charisma_str = self._extract_content('cha-value', atr_name='id')
        charisma_int = ContextInterpreter._content_to_int(charisma_str, regex_pattern=r'\d+')
        return charisma_int
    
    def get_stat_block(self):
        return self._extract_body('field--name-field-monster-stat-block')
    
    def get_description(self):
        return self._extract_content('field--name-field-monster-description')
    
    def get_behavior(self):
        return self._extract_content('field--name-field-monster-behavior')
    
    def get_encounters(self):
        return self._extract_content('field--name-field-monster-encounters')
    
    def get_type_description(self):
        return self._extract_content('field--name-field-monster-type-description')
    
    def get_source(self):
        return self._extract_content('field--name-field-monster-source')