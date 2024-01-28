import re
from data_forge.data_interpreters.context_interpreter import ContextInterpreter


class CombatManeuverInterpreter(ContextInterpreter):
    def __init__(self, source_code : str):
        super().__init__(source_code)
    
    def get_exertion_points(self):
        points_action_str = self._extract_content('combat-maneuver-points-actions')
        points = str(re.search(r'(?<=\().+(?=[\s\n]* points?\))', points_action_str).group())
        return points

    def get_prerequisite(self):
        return self._extract_content('combat-maneuver-prerequisite')

    def get_body(self):
        return self._extract_body('field--name-body')
    
    def get_source(self):
        return self._extract_content('field--name-field-cm-source')

    def get_degree(self):
        degree_tradition_str = self._extract_content('combat-maneuver-degree-tradition-action-type')
        degree_pattern = r'\d+\w+ degree|Basic maneuver'
        degree = re.search(degree_pattern, degree_tradition_str).group()
        return degree
    
    def get_tradition(self):
        degree_tradition_str = self._extract_content('combat-maneuver-degree-tradition-action-type')
        degree = self.get_degree()
        tradition = degree_tradition_str.replace(degree, "").strip()
        return tradition


