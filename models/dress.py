#!/usr/bin/python3
"""This module implements the dress feature of the dress_me_up app.
Listing the different options like trousers, shirts, Tees, gowns,
and others.
"""
import models
from models.event import Event
from models.parent_model import ParentModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Dress(ParentModel, Base):
    """This class inherits from the parent model to share methods
    and attributes.
    """
    __tablename__ = 'dresses'

    if models.storage_type == "db":
        name = Column(String(128), nullable=False)
        description = Column(String(128), nullable=False)
        brand = Column(String(128), nullable=False)
        category = Column(String(128), nullable=False)
        image = Column(String(128), nullable=False)
        # event_id = Column(String(60), ForeignKey('events.id'), nullable=False)
        event = relationship('Event', backref='dresses', cascade='all')
    else:
        name = ""
        description = ""
        brand = ""
        category = ""
        image = ""


    def __init__(self, *args, **kwargs):
        """This method initializes all the attributes and fields
        implemented on the class.
        """

        super().__init__(*args, **kwargs)
