
import os

from data_forge.data_interpreters.table_interpreter import TableInterpreter

from data_forge.data_structures.card import Card
from data_forge.data_structures.combat_maneuver import CombatManeuver
from data_forge.data_structures.magic_item import MagicItem
from data_forge.data_structures.spell import Spell
from data_forge.data_structures.feat import Feat
from data_forge.file_handlers.file_handler import FileHandler

# This class extracts a list of data structures from a table
class TableToDataStructure:
    def __init__(self, card_type:str):
        self.card_type = card_type

    # This function extracts a list of data structures from a table
    def make_data_structures(self, table_extractor : TableInterpreter) -> list[Card]:
        list_of_names = table_extractor.extract_list_of_names_with_link()
        if self.card_type == Spell.__name__:
            list_of_summaries = table_extractor.extract_list_of_summaries()

        card_data_list : list[Card] = []
        
        for i in range(len(list_of_names)):
            print(f"Making a {self.card_type} data structure for {list_of_names[i][0]}...")

            if self.card_type == Spell.__name__:
                card = self.__make_card_data(list_of_names[i][0], list_of_names[i][1], list_of_summaries[i])
            else:
                card = self.__make_card_data(list_of_names[i][0], list_of_names[i][1])

            card_data_list.append(card)

        return card_data_list

    # This function makes a card data structure
    def __make_card_data(self, title : str, summary : str = "") -> Spell|Feat|CombatManeuver|Card:
        source_code = FileHandler.read_file(FileHandler.get_card_source_code_directory(self.card_type, title))
        match self.card_type:
            case Spell.__name__:
                card = Spell(
                    title=title,
                    source_code=source_code,
                    summary=summary
                )
            case Feat.__name__:
                card = Feat()
            case CombatManeuver.__name__:
                card = CombatManeuver()
            case MagicItem.__name__:
                card = MagicItem(
                    title=title,
                    source_code=source_code
                    )
            case _:
                raise ValueError(f"ERROR! {self.card_type} is not a valid type!")

        return card
