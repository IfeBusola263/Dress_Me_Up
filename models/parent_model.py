#!/usr/bin/python3
"""This module is the parent model for other models tracked in the app.
"""

from uuid import uuid4
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
import models
from sqlalchemy import String, Column, DateTime

# The declarative base is a straight forward way to create the tables
# from the schemas created in a python class through ORM.
Base = declarative_base()


class ParentModel():
    """This is the parent model for other models
    """

    __models = {}
    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        """At the creation of the instance of this class, this function
        runs first, and it's useful for setting up the attributes and
        fields of the class.
        """

        if kwargs:
            if not kwargs.get('__class__') and kwargs.get('id'):
                del kwargs['id']

            if not kwargs.get('__class__') and kwargs.get(
                    'created_at') and kwargs.get('updated_at'):
                del kwargs['created_at']
                del kwargs['updated_at']

            if kwargs.get('__class__'):
                del kwargs['__class__']

            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    kwargs[key] = datetime.strptime(kwargs[key],
                                                    '%Y-%m-%dT%H:%M:%S.%f')
                setattr(self, key, value)

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

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
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def delete(self):
        """This method deletes the instance of this class.
        """
        models.storage.delete(self)
        models.storage.save()
