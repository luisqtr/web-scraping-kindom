import json, pickle

def load_json(json_path = "folder_tree.json"):
    """
    Loads in memory a structured dictionary with the filenames of the
    files where the main data is located within the compressed dataset.

    :param json_path: Path of JSON file with the dictionary
    :type json_path: str
    :return: Loaded JSON file 
    :rtype: dict
    """
    with open(json_path, "r") as json_file:
        files_index = json.load(json_file)
        # Check number of users loaded
        return files_index


def create_json(dictionary, json_path = "folder_tree.json", indent=None):
    """
    Create a structured dictionary with the filenames of the
    files where the main data is located within the compressed dataset.

    :param json_path: Destination path of JSON file with the dictionary
    :type json_path: str
    :return: Loaded JSON file 
    :rtype: JSON
    """
    with open(json_path, "w") as json_file:
        json.dump(dictionary, json_file, indent=indent)
        print("JSON file was created in", json_path)
        return json_file


def load_pickle(file_path = "data.pickle"):
    """
    Creates a binary object with the data of movements

    :param file_path: Path of pickle file
    :type file_path: str
    :return: Serialized object
    :rtype: object
    """
    with open(file_path, "rb") as readFile:
        data = pickle.load(readFile)
        return data


def create_pickle(data_to_save, file_path = "data.pickle"):
    """
    Creates a binary object with the data of movements

    :param data_to_save: Python object to serialize
    :type data_to_save: object
    :param file_path: Path to save serialized object
    :type file_path: str
    :return: None
    :rtype: None
    """
    with open(file_path, "wb") as writeFile:
        pickle.dump(data_to_save, writeFile)