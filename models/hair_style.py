#!/usr/bin/python3
"""This module implements the hair style model for the dress me up app
"""
import models
from models.parent_model import ParentModel, Base
from sqlalchemy import String, Column, Integer


class HairStyle(ParentModel, Base):
    """This class models the hair style for the app.
    """

    __tablename__ = 'hair_style'

    if models.storage_type == "db":
        name = Column(String(128), nullable=False)
        description = Column(String(128), nullable=False)
        lenght = Column(Integer, nullable=False)
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
