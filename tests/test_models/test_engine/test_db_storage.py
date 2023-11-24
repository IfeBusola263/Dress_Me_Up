import unittest
from models.dress import Dress
from models.user import User
from models.engine.db_storage import DBStorage
from models import storage, storage_type
from models.parent_model import ParentModel
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from os import getenv


class testEngine(unittest.TestCase):
    """Creates a class for testing the db storage engine"""
    def setUp(self):
        """Sets up the instances"""
        self.db_storage = DBStorage()
        self.db_storage.reload()
        self.inst_dict = {"name": "Short Chic",
                          "description": "simple and smart",
                          "brand": "Dolce & Gabanna",
                          "category": "casual",
                          "image": "some/path"}
        self.dressInstance = Dress(**self.inst_dict)
        self.userInstance = User()
        self.userInstance.name = "DressMe"
        self.userInstance.email = "dress_me@me"
        self.userInstance.measurement = "20"
        self.userInstance.outfits = "some_outfit"
        self.userInstance.country = "planet nation"
        self.userInstance.state = "United state"
        self.userInstance.password = "access allowed"

    def tearDown(self):
        """Drops all table after each test"""
        # self.session.close()
        # self.engine.dispose()
        pass

    def test_save(self):
        """Test the save() method in the DBStorage class"""
        self.db_storage.new(self.dressInstance)
        result = self.db_storage.save()
        self.db_storage.new(self.userInstance)
        new_user = self.db_storage.save()
        self.assertIsNone(result)
        self.assertIsNone(new_user)
        self.assertNotEqual(self.dressInstance.id, None)

    def test_all(self):
        """Test for the all() method of the DBStorage class"""
        all_user = self.db_storage.all(User)
        self.assertNotEqual(len(all_user), 0)


if __name__ == '__main__':
    unittest.main()
