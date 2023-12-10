from data_forge.data_structures.card import Card

class Feat(Card):
    def __init__(self,
            name: str = "", origin: str = "", summary: str = "", prerequisites: str = "", description: str = ""):
        self.name = name
        self.origin = origin
        self.summary = summary
        self.prerequisites = prerequisites
        self.description, self.sub_feats = SubFeat.divideDescription(description)


class SubFeat:
    def __init__(self,
            name: str = "", description: str = ""
            ):
        self.name = name
        self.description = description
    

# TODO: Implement this
def divideDescription(text: str) -> (str, list[SubFeat]):
    body = ""
    sub_feats = []
    
    # split text into body and sub-feats
    return body, sub_feats