import os
import pickle
from data_forge.data_structures.context import Context
from data_forge.file_handlers.file_handler import FileHandler

class ObjectSaver(FileHandler):
    def save_object(obj):
        abs_filepath = ObjectSaver.__generate_filepath(obj, "Pickled")
        abs_filepath = FileHandler._make_file_if_not_exists(abs_filepath, ".pkl")
        
        with open(abs_filepath, 'wb') as file:
            pickle.dump(obj, file)
        print(f'Object successfully saved to "{abs_filepath}"')


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

    def save_object_string(obj:Context):
        filepath = ObjectSaver.__generate_filepath(obj, "String")
        FileHandler.write_to_file_absolute_path(str(obj), filepath, ".txt")
        

    def __generate_filepath(obj, type_:str):
        return f"Outputs\\Saved_Data\\{type(obj).__name__}s\\{type_}s\\{obj.data_name}"