import os
import pickle

from FileHandler import FileHandler

def save_object(obj):
    filepath = generate_filepath(obj)

    FileHandler.make_file_if_not_exists(filepath)
    
    with open(filepath, 'wb') as file:
        pickle.dump(obj, file)
        file.close()
    
    filename = filepath.split('\\')[-1]
    print(f'Object successfully saved to "{filename}"')

def load_object(filename:str, type:str):
    filepath = f"FileHandler\\Saved_Data\\{type.capitalize()}\\{filename}.pkl"
    if os.path.exists(filepath):

        with open(filepath, 'rb') as file:
            obj = pickle.load(file)
            file.close()
        
        filename = filepath.split('\\')[-1]
        print(f'Object successfully loaded from "{filename}"')
        return obj
    
    else:
        print(f'Object "{filename}" does not exist')
        return None

def generate_filepath(obj):
    return f"FileHandler\\Saved_Data\\{type(obj).__name__}\\{obj.name}.pkl"