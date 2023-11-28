#!/usr/bin/python3
"""
This is the model that holds the user class
"""
from models.parent_model import ParentModel, Base
from sqlalchemy import Column, String
from models import storage_type
import hashlib

class User(ParentModel, Base):
    """This is the instance representation for the user object"""

    __tablename__ = 'users'
    if storage_type == 'db':

        name = Column(String(60), nullable=False)
        email = Column(String(120), nullable=False)
        profile_picture = Column(String(60), nullable=True)
        preference = Column(String(120), nullable=True)
        measurement = Column(String(60), nullable=False)
        outfits = Column(String(60), nullable=False)
        country = Column(String(60), nullable=False)
        state = Column(String(60), nullable=False)
        password = Column(String(120), nullable=False)

    else:
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
        if 'password' in kwargs:
            self.password = self._hash_password(self.password)

    def _hash_password(self, password):
        """Functionality to hash password"""
        md5 = hashlib.md5()
        md5.update(password.encode('utf-8'))
        return md5.hexdigest()

