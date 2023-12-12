from data_forge.data_structures.card import Card

field_classes = [
    "field--name-field-monster-size",
    "field--name-field-monster-type",
    "field--name-field-monster-challenge-rating",
    "field--name-field-monster-terrain",
    "field--name-field-monster-stat-block"

]

field_ids = [
    "str-value",
    "dex-value",
    "con-value",
    "int-value",
    "wis-value",
    "cha-value"
]

class Monster(Card):
    def __init__(self, title : str, source_code : str):
        super(Monster, self).__init__(title, source_code, field_classes, field_ids)

        self.set_fields(self.extract_fields())
    
    def set_fields(self, field_dict : dict):
        self.size = field_dict.get("size")
        self.type = field_dict.get("type")
        self.challenge_rating = field_dict.get("challenge_rating")
        self.terrain = field_dict.get("terrain")
        self.stat_block = field_dict.get("stat_block")
        self.str = field_dict.get("str")
        self.dex = field_dict.get("dex")
        self.con = field_dict.get("con")
        self.int = field_dict.get("int")
        self.wis = field_dict.get("wis")
        self.cha = field_dict.get("cha")

    # This function generates a key name from a field class or id
    def key_namer(self, key : str):
        key_name = key.lower()
        for ch in ["monster-", "-value"]:
            key_name = key_name.replace(ch,"")
        
        key_name = super(Monster, self).key_namer(key_name)

        return key_name