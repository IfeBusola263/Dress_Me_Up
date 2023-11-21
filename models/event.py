#!/usr/bin/python3
"""Creates a model for various kinds
   of events
"""
import models
from models.parent_model import ParentModel, Base
from sqlalchemy import Column, String


class Event(ParentModel, Base):
    """Creates an Event class"""
    if models.storage_type == "db":
        __tablename__ = 'events'
        event_id = Column(String(60), nullable=False)
        name = Column(String(128), nullable=False)

    else:
        event_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        """Instantiate object with given attributes"""
        super().__init__(*args, **kwargs)

    def __str__(self):
        """Returns the string representation of class instance"""
        return f"[{self.__class__.__name__}] {self.__dict__}"
