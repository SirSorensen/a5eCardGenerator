
class SubFeat:
    def __init__(self,
            name: str = "", description: str = ""
            ):
        self.name = name
        self.description = description
    
def divideDescription(text: str) -> (str, list[SubFeat]):
    body = ""
    sub_feats = []
    
    # split text into body and sub-feats
    return body, sub_feats


class Feat:
    def __init__(self,
            name: str = "", origin: str = "", summary: str = "", prerequisites: str = "", description: str = ""):
        self.name = name
        self.origin = origin
        self.summary = summary
        self.prerequisites = prerequisites
        self.description, self.sub_feats = divideDescription(description) 


