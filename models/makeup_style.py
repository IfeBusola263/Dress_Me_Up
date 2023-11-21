#!/usr/bin/python3
"""
This is the model that holds the makeup style class
"""

from models.parent_model import ParentModel


class MakeupStyle(ParentModel):
    """THis is the instance representation for the makeup style object"""
    name = ""
    description = ""
    makeup_type = ""
    image = ""
    
    def __init__(self, *args, **kwargs):
        """initializes MakeupStyle"""
        super().__init__(*args, **kwargs)

    
