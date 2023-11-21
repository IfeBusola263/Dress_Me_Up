#!/usr/bin/python3
"""This module is the parent model for other models tracked in the app.
"""

from uuid import uuid4
from datetime import datetime

class ParentModel():
    """This is the parent model for other models
    """

    __models = {}

    def __init__(self):
        """At the creation of the instance of this class, this function
        runs first, and it's useful for setting up the attributes and
        fields of the class.
        """
        from models import storage
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        storage.new(self)

    def __str__(self):
        """This method returns a string representation of the model.
        """
        attr = {key:value for key, value in self.__dict__.items() if key != 'id'}
        return f'[{self.__class__.__name__}] ({self.id}) {attr}'


    def make_json(self):
        """This method extracts the attributes of the object and
        returns the dictionary representation of the object, to aid
        conversion to json.
        """
        attr = {key:value for key, value in self.__dict__.items()}
        # attr = self.__dict__.copy()
        attr['created_at'] = self.created_at.isoformat()
        attr['updated_at'] = self.updated_at.isoformat()
        attr['__class__'] = self.__class__.__name__
        # attr['id'] = self.id
        return attr

    def save(self):
        """This method, save the instance of the model in a dedicated
        storage. Either a database of a file storage.
        """
        from models import storage
        self.updated_at = datetime.now()
        storage.save()
