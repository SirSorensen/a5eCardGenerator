import unittest
import data_forge.data_structures.context as Context


# # This function converts a card's name to a data name, by replacing spaces and special characters with underscores or nothing
#     def name_to_data_name(name : str):
#         data_name = name.lower()
#         data_name = re.sub(r"\s| |\\|\/|\{|\}|\[|\]|\(|\)|\>|\#|\+|\:|\!|\?|\&|\||\<", "_", data_name)
#         data_name = re.sub(r"\`|\´|\*|\’|\'|\"", "", data_name)
#         return data_name


class TestCardData(unittest.TestCase):
    # Test that the function returns the correct data name for a card with a name that contains no special characters
    def test_name_to_data_name(self):
        # Arrange
        test_card_name_1 = "Test Card"
        test_card_name_2 = "Test/Card"

        # Act
        test_card_data_name_1 = Context.Context.name_to_data_name(test_card_name_1)
        test_card_data_name_2 = Context.Context.name_to_data_name(test_card_name_2)

        # Assert
        self.assertEqual(test_card_data_name_1, "test_card")
        self.assertEqual(test_card_data_name_2, "test_card")

print("Running CardData_Tests.py")