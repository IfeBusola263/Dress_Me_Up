#!/usr/bin/python3
"""This module implements the hair style model for the dress me up app
"""
import models
from models.parent_model import ParentModel, Base
from sqlalchemy import String, Column, Integer


class HairStyle(ParentModel):
    """This class models the hair style for the app.
    """
    if models.storage_type == "db":
        __tablename__ = 'hair_style'
        name = Column(String(128), nullable=False)
        description = Column(String(128), nullable=False)
        lenght = Column(Integer(60), nullable=False)
        image = Column(String(128), nullable=False)
    else:
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
