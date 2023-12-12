from data_forge.data_structures.card import Card

field_classes = [
    "feat-prerequisite",
    "feat-details",
    "feat-source"
]

field_ids = []

class Feat(Card):
    def __init__(self, title : str, source_code : str):
        super(Feat, self).__init__(title, source_code, field_classes, field_ids)

        self.set_fields(self.extract_fields())
    
    def set_fields(self, field_dict : dict):
        # self.origin = field_dict.get('origin')
        # self.summary = field_dict.get('summary')
        self.prerequisites = field_dict.get('prerequisite')
        self.description, self.sub_feats = SubFeat.divideDescription(field_dict.get('details'))
        self.source = field_dict.get('source')

    # This function generates a key name from a field class or id
    def key_namer(self, key : str):
        key_name = key.lower()
        for ch in ["feat-"]:
            key_name = key_name.replace(ch,"")
        
        key_name = super(Feat, self).key_namer(key_name)

        return key_name

class SubFeat:
    def __init__(self,
            name: str = "", description: str = ""
            ):
        self.name = name
        self.description = description
    

# TODO: Implement this
def divideDescription(text: str) -> (str, list[SubFeat]):
    body = text
    sub_feats = []
    
    # split text into body and sub-feats
    return body, sub_feats

