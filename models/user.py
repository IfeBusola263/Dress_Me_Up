#!/usr/bin/python3
"""
This is the model that holds the user class
"""
from models.parent_model import ParentModel


class User(ParentModel):
    """THis is the instance representation for the user object"""
    name = ""
    email = ""
    profile_picture = ""
    preference = ""
    measurement = ""
    outfits = ""
    country = ""
    state = ""
    password = ""
    
    def __init__(self, *args, **kwargs):
        """initializes User"""
        super().__init__(*args, **kwargs)
