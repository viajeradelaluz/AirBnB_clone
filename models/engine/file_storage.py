#!/usr/bin/python3
"""
File Storage class
"""

import json
import os

class FileStorage():
    """
    File Storage engine for HBnB
    """
    __file_path = "file.json"
    __objects = dict()

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj
    
    def save(self):
        new_dict = {}
        for (key, value) in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, mode='w') as jsonfile:
            json.dump(new_dict, jsonfile)

    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, mode='r') as jsonfile:
                create_dict = json.load(jsonfile)
                for (key, value) in create_dict:
                    self.__objects = """???"""
