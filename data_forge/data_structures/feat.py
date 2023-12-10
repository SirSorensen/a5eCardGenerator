from data_forge.data_structures.card import Card

field_classes = []

field_ids = []

class Feat(Card):
    def __init__(self, title : str, source_code : str):
        # Title = "*"
        self.title = title

        super(Feat, self).__init__(title, source_code, field_classes, field_ids)

        self.set_fields(self.extract_fields())
    
    def set_fields(self, field_dict : dict):
        return
        self.name = field_dict.get('name')
        self.origin = field_dict.get('origin')
        self.summary = field_dict.get('summary')
        self.prerequisites = field_dict.get('prerequisites')
        self.description, self.sub_feats = SubFeat.divideDescription(field_dict.get('description'))


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

