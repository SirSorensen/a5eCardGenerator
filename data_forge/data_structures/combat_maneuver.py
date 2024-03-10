import re
from data_forge.data_interpreters.card_interpreters.combat_manuever_interpreter import CombatManeuverInterpreter
from data_forge.data_structures.card import Card
from data_forge.data_structures.context_contents import Paragraphs
from data_forge.settings import *



class CombatManeuver(Card):
    def __init__(self, id : str, title : str, source_code : str, summary : str):
        # Summary = "*"
        self.summary = summary
        super(CombatManeuver, self).__init__(id, title, source_code)
    
    def set_fields(self, source_code : str):
        code_interpreter = CombatManeuverInterpreter(source_code)
        self.exertion_points = code_interpreter.get_exertion_points()
        self.prerequisite = code_interpreter.get_prerequisite()
        self.body = code_interpreter.get_body()
        self.source = code_interpreter.get_source()
        self.degree = code_interpreter.get_degree()
        self.tradition = code_interpreter.get_tradition()

    
    def set_text_fields(self):
        self.subtitle = str(self.degree)
        self.subtitle += f", {str(self.tradition)}" if self.tradition else ""

        self.description : Paragraphs = self.body
        self.icon = ""
        self.image = ""

        if not (self.title and self.subtitle and self.description):
            raise ValueError(f"Missing required fields for {self.name}:\n{self}\nTitle: {self.title}\nSubtitle: {self.subtitle}\nDescription: {self.description}")