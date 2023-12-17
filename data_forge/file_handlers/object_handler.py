from data_forge.settings import *
import os
import pickle
from data_forge.file_handlers.file_handler import FileHandler
from data_forge.data_structures.card import Card

global_pickled_output_directory = rf"{FileHandler._get_global_output_directory()}Pickled/"

class ObjectHandler(FileHandler):

    # Returns the objects's pickled object's file path = abs_filepath
    def save_object(obj, abs_filepath : str = None):
        obj_name = obj.__class__.__name__

        if abs_filepath is None:
            abs_filepath = ObjectHandler.gen_pickled_object_filepath(obj_name)

        FileHandler._make_file_if_not_exists(abs_filepath)
        
        with open(abs_filepath, 'wb') as pickle_file:
            pickle.dump(obj, pickle_file)
        
        if debug: print(f'{obj_name} successfully saved to "{abs_filepath}"')

        return abs_filepath
    

    # Loads the object from the given file path
    # Returns the object if it exists, else returns None
    def load_object(abs_filepath):
        if os.path.exists(abs_filepath):
            with open(abs_filepath, 'rb') as file:
                obj = pickle.load(file)
                file.close()
            if debug: print(f'Object successfully loaded from "{abs_filepath}"')
            return obj
        else:
            print(f'Object "{abs_filepath}" does not exist')
            return None



    def save_card_if_not_exists(card : Card):
        context_name = card.name
        card_type = card.__class__.__name__

        abs_filepath = ObjectHandler.gen_pickled_card_filepath(card_type, context_name)
        if not FileHandler.does_file_exist(abs_filepath):
            ObjectHandler.save_object(card, abs_filepath)
            if debug: print(f'Pickled card "{context_name}" successfully saved')
        else:
            if debug: print(f'Pickled card "{context_name}" already exists')
        
        return abs_filepath

    def load_card(card_type : str, context_name : str):
        abs_filepath = ObjectHandler.gen_pickled_card_filepath(card_type, context_name)
        return ObjectHandler.load_object(abs_filepath)
    


    
    def gen_pickled_object_filepath(obj_name : str):
        return rf"{global_pickled_output_directory}{obj_name}.pkl"
    
    def gen_pickled_card_filepath(card_type : str, context_name : str):
        return rf"{global_pickled_output_directory}{card_type}s/{context_name}.pkl"
    
    def gen_pickled_card_dict_filepath():
        return rf"{global_pickled_output_directory}card_dict.pkl"
