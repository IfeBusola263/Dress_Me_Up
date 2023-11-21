#!/usr/bin/python3
"""Creates a model for various kinds
   of events
"""

from models.parent_model import ParentModel



class Event(ParentModel):
    """Creates an Event class"""
    event_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Instantiate object with given attributes"""
        super().__init__(*args, **kwargs)

    def __str__(self):
        """Returns the string representation of class instance"""
        return f"[{self.__class__.__name__}] {self.__dict__}"
