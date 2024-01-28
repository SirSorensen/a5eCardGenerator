import re
from data_forge.data_interpreters.context_interpreter import ContextInterpreter


class SpellInterpreter(ContextInterpreter):
    def __init__(self, source_code : str):
        super().__init__(source_code)

    def get_level(self) -> int:
        level_str = self._extract_content('field--name-field-spell-level')
        int_match = re.search(r'\d+', level_str)
        if int_match is None:
            cantrip_match = re.search(r'cantrip', level_str.lower())
            if cantrip_match is None:
                raise ValueError(f"Unknown level for {level_str}")
            else:
                return 0
        level_int = int(int_match.group())

        return level_int

    def get_classical_school(self):
        return self._extract_content('field--name-field-classical-spell-school')
    
    def get_schools(self):
        return self._extract_content_list('field--name-field-spell-schools')

    def get_classes(self):
        return self._extract_content_list('field--name-field-spell-classes')

    def get_casting_time(self):
        return self._extract_content('field--name-field-spell-casting-time')

    def get_ritual(self):
        return self._contains_element_with_atr('class', 'ritual-indicator')

    def get_range(self):
        return self._extract_content('field--name-field-spell-range')

    def get_target(self):
        return self._extract_content('field--name-field-spell-target')

    def get_area(self):
        area_str = self._extract_content('field--name-field-spell-area')
        area_int = ContextInterpreter._content_to_int(area_str, regex_pattern=r'\d+')
        return area_int

    def get_area_shape(self):
        return self._extract_content('field--name-field-area-shape')

    def get_component_material(self):
        return self._contains_element_with_atr('href', '/spell-components/material')

    def get_component_seen(self):
        return self._contains_element_with_atr('href', '/spell-components/seen')

    def get_component_vocalized(self):
        return self._contains_element_with_atr('href', '/spell-components/vocalized')

    # TODO: Check if consumed or have a gp value
    def get_component_material_components(self):
        material_components_str = self._extract_content('field--name-field-spellcomponent-description')

        has_gp_value = re.search(r'at least [\d\,\.]+ gold', material_components_str) is not None
        is_consumed = re.search(r'\bconsumed by the spell?\b', material_components_str) is not None

        return material_components_str, has_gp_value, is_consumed

    def get_duration(self):
        return self._extract_content('duration-value', 'span')
    
    def get_concentration(self):
        duration_content = self._extract_content('duration', atr_name='id')
        return 'Concentration' in duration_content

    def get_saving_throw_desc(self):
        return self._extract_content('field--name-field-spell-saving-throw-desc')

    def get_body(self):
        return self._extract_body('field--name-body')

    def get_spellcast_at_higher_levels(self):
        return self._extract_content('field--name-field-spellcast-at-higher-levels')

    def get_rare_versions(self):
        return self._extract_content_list('field--name-field-spell-rare-versions')

    def get_source(self):
        return self._extract_content('field--name-field-spell-source')

