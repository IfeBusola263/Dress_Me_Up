#!/usr/bin/python3
"""Creates a model for various kinds
   of events
"""
import models
from models.parent_model import ParentModel, Base
from sqlalchemy import Column, String, ForeignKey


class Event(ParentModel, Base):
    """Creates an Event class"""
    __tablename__ = 'events'

    if models.storage_type == "db":
        #event_id = Column(String(60), primary_key=True, nullable=False)
        name = Column(String(128), nullable=False)
        dress_id = Column(String(60), ForeignKey('dresses.id'), nullable=False)

    else:
        dress_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        """Instantiate object with given attributes"""
        super().__init__(*args, **kwargs)

    # def __str__(self):
    #     """Returns the string representation of class instance"""
    #     return f"[{self.__class__.__name__}] {self.__dict__}"
