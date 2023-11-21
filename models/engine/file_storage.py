#!/usr/bin/python3
"""Create a file storage engine model
   for storage of creates instances
"""

from models.parent_model import ParentModel
import models
import json
import os


class FileStorage():
    """Creates a class FileStorage"""
    __file_path = './file.json'
    __obj_dict = {}

    def all(self, cls=None):
        """A method that returns all classes
           create instances
        """
        if cls is not None:
            cls_obj = {}
            for key, value in self.__obj_dict.items():
                """
                   #User.1234567  {(created_at, id, __class__)}
                   we loop through the obj_dict and get
                   it's keys and values. we go into the
                   value which itself is a dictionary and check
                   if the cls passes as argument is in that dictionary
                   by doing value.__class__. If it is there, we set
                   the new cls_obj[key] to the value
                """
                if cls == value.__class__:
                    cls_obj[key] = value
            return cls_obj
        return self.__obj_dict

    def new(self, obj=None):
        """A method that creates a new instance
        of a class
        """
        cls = obj.__class__.__name__
        key = f"{cls}.{obj.id}"
        self.__obj_dict[key] = obj

    def save(self):
        """A method that stores a newly created
           instance
        """
        obj_json = {}
        
        for key, value in self.__obj_dict.items():
            obj_json[key] = value.make_json()
            
        with open(self.__file_path, 'w') as f:
            json.dump(obj_json, f)

    def reload(self):
        """A method that reloads a file"""
        file = self.__file_path

        if os.path.exists(file):
            with open(file, 'r') as f:
                json.load(f)

    def delete(self, obj=None):
        """Erase an object from file storage"""
        if obj is None:
            key = f'{obj.__class__.name__}.{obj.id}'
            del self.__obj_dict[key]
            storage.save()
