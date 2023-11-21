#!/usr/bin/python3
"""This module implements the hair style model for the dress me up app
"""

from models.parent_model import ParentModel


class HairStyle(ParentModel):
    """This class models the hair style for the app.
    """
    name = ""
    description = ""
    length = 0
    image = ""

    def __init__(self, *args, **kwargs):
        """This method initializes the fields and attribute of the
        hairstyle class and inherits the fields and methods from the
        parent class ParentModel.
        """

        super().__init__(*args, **kwargs)
