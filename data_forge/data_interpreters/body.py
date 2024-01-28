from bs4 import Tag
from data_forge.data_interpreters.code_interpreter import CodeInterpreter

class Body(CodeInterpreter):
    def __init__(self, body_tag : Tag):
        self.tag = body_tag
    
