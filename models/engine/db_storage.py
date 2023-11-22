#!/usr/bin/python3
"""Creates a model for storing object
   creation to mysql database
"""
import models
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from os import getenv


class DBStorage:
    """Creates a storage class using ORM and
       MySQLdb
    """
    __session = None
    __engine = None

    def __init__(self):
        """Instantiate object with state attributes"""
        password = getenv("DRESS_ME_MYSQL_PWD")
        localhost = getenv("DRESS_ME_MYSQL_HOST")
        db_name = getenv("DRESS_ME_MYSQL_DB")
        db_user = getenv("DRESS_ME_MYSQL_USER")

        self.__engine = create_engine(
                'mysql+mysqldb://{}:{}@{}/{}'.format(
                    db_user, password, localhost, db_name),
                pool_pre_ping=True)

    def all(self, cls=None):
        """A method that returns all class object"""
        db_object = {}

        if cls is not None:
            # Querying all the objects of a particular class
            objs = self.__session.query(cls).all()
            for obj in objs:
                class_name = obj.__class__.__name__
                key = f"{class_name}.{obj.id}"
                db_object[key] = obj
        else:
            for key, value in models.classes.items():
                objs = self.__session.query(value).all()
                for obj in objs:
                    obj_key = f"{key}.{obj.id}"
                    db_object[obj_key] = obj
        return db_object

    def reload(self):
        """Starts a session for the sqlalchemy"""
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def new(self, obj=None):
        """Adds an instance to a database"""
        self.__session.add(obj)

    def save(self):
        """Stores an object in the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Removes an object from the database"""
        self.__session.delete(obj)

    def close(self):
        """Closes an open session"""
        self.__session.close()
