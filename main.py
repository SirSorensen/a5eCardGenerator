import os
import sys
from main_methods import *
from Printer.card_png import make_cards

# clean_up_and_remake_data()
test_insert_input_into_power_point()


# Make slides into printable version
make_cards()

# source_code_path = r'Outputs\\HTML\\CombatManeuvers\Source_Code\\agile_feint.html'
# source_code = FileHandler.read_file(source_code_path)
# context_interpreter = ContextInterpreter(source_code)
# element = context_interpreter.soup.find('div', class_='field--name-body')
# print(element.get('class'))
# paragraphs = context_interpreter._extract_body('combat-maneuver-body')
# print(paragraphs)