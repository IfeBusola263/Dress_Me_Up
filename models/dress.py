#!/usr/bin/python3
"""This module implements the dress feature of the dress_me_up app.
Listing the different options like trousers, shirts, Tees, gowns,
and others.
"""

from models.parent_model import ParentModel

class Dress(ParentModel):
    """This class inherits from the parent model to share methods
    and attributes.
    """
    name = ""

    def __init__(self):
        """This method initializes all the attributes and fields
        implemented on the class.
        """

        super().__init__()
