
from openpyxl import Workbook
from data_forge.settings import *
from data_forge.data_structures.card import Card

class SheetMaker:
    def __init__(self, sheet_name):
        self.sheet_name = sheet_name
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.title = self.sheet_name

    def add_row(self, row):
        self.ws.append(row)

    def save(self, file_name):
        self.wb.save(file_name)
    
    def save_card_titles(self, card : Card):
        # Create an empty list to store field name and value pairs
        fields = []

        # Iterate through all the attributes of the class
        for attr_name, attr_value in vars(card).items():
            # Exclude private attributes (those starting with underscores)
            if not attr_name.startswith('_'):
                if type(attr_value) == str or type(attr_value) == int:
                    fields.append(str(attr_name))
        
        # Add the row of field names to the sheet
        self.add_row(fields)
    
    def insert_card_properties(self, card : Card):
        # Create an empty list to store field name and value pairs
        field_values = []

        # Iterate through all the attributes of the class
        for attr_name, attr_value in vars(card).items():
            # Exclude private attributes (those starting with underscores)
            if not attr_name.startswith('_'):
                if type(attr_value) == str or type(attr_value) == int:
                    field_values.append(str(attr_value))
        
        self.add_row(field_values)