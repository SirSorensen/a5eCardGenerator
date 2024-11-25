from data_forge.data_interpreters.card_interpreters.feat_interpreter import FeatInterpreter
from data_forge.data_structures.card import Card
from data_forge.data_structures.context_contents import Paragraphs
from data_forge.settings import *


class Feat(Card):
    def __init__(self, id : str, title : str, source_code : str):
        super(Feat, self).__init__(id, title, source_code)
    
    def set_fields(self, source_code : str):
        code_interpreter = FeatInterpreter(source_code)
        self.feat_synergy = code_interpreter.get_feat_synergy()
        self.prerequisite = code_interpreter.get_prerequisite()
        self.body = code_interpreter.get_body()
        self.source = code_interpreter.get_source()
    

    def set_text_fields(self):
        self.subtitle = str(self.prerequisite)
        self.icon = ""
        self.image = ""

class SubFeat:
    def __init__(self,
            name: str = "", description: str = ""
            ):
        self.name = name
        self._description = description
    

    # TODO: Implement this
    def divideDescription(text: str):
        body = text
        sub_feats = []
        
        # split text into body and sub-feats
        return body, sub_feats

    