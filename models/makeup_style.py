#!/usr/bin/python3
"""
This is the model that holds the makeup style class
"""

from models.parent_model import ParentModel, Base
from sqlalchemy import Column, String
from models import storage_type


class MakeupStyle(ParentModel, Base):
    """This is the instance representation for the makeup style object"""

    __tablename__ = 'makeup_styles'

    if storage_type == 'db':
        name = Column(String(120), nullable=False)
        description = Column(String(120), nullable=False)
        makeup_type = Column(String(60), nullable=False)
        image = Column(String(60), nullable=False)
    else:
        name = ""
        description = ""
        makeup_type = ""
        image = ""

    def __init__(self, *args, **kwargs):
        """initializes MakeupStyle"""
        super().__init__(*args, **kwargs)

    
