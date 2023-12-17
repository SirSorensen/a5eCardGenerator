
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
                fields.append(str(attr_name).capitalize())
                    
        

        fields.append("Amount")
        
        # Add the row of field names to the sheet
        self.add_row(fields)
    
    def insert_card_properties(self, card : Card):
        # Create an empty list to store field name and value pairs
        field_values = []

        # Iterate through all the attributes of the class
        for attr_name, attr_value in vars(card).items():
            # Exclude private attributes (those starting with underscores)
            if not attr_name.startswith('_'):

                if attr_value == None or str(attr_value) == "" or (type(attr_value) == list and len(attr_value) == 0):
                    field_values.append("-")
                else:
                    field_values.append(str(attr_value))

        field_values.append(0)

        print(f"Found {len(field_values)} fields")
        if len(field_values) < 24:
            print(f"Error: {card.title} has {len(field_values)} fields")
            print(str(field_values))
            return
        
        self.add_row(field_values)
    
    def hide_irrelevant_column(self):
        for row in self.ws.iter_rows(min_row=1, max_col=20, max_row=1):
            for cell in row:
                if cell.value != "Title" and cell.value != "Amount":
                    self.ws.column_dimensions[cell.column_letter].hidden = True
        