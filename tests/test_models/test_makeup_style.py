#!/usr/bin/python3
"""This is a unittest for the parent model.
"""

import unittest
from models.makeup_style import MakeupStyle
import sys
from io import StringIO

class TestMakeupStyle(unittest.TestCase):
    """This is a unit for the parent model. For all attributes
    and methods in the class.
    """

    def setUp(self):
        """This class sets up an instance of the class which the test will run on.
        """
        self.obj_1 = MakeupStyle()
        del self.obj_1.__dict__['_sa_instance_state']
        self.obj_2 = MakeupStyle(name="Something")
        del self.obj_2.__dict__['_sa_instance_state']
        attr = {"name": "something", "id": 657857}
        self.obj_3 = MakeupStyle(**attr)
        del self.obj_3.__dict__['_sa_instance_state']

        self.assertEqual(self.obj_2.name, "Something")
        self.assertEqual(self.obj_3.name, "something")
        self.assertNotEqual(self.obj_3.id, attr['id'])

    def test_str(self):
        """Test for the string representation of the models
        """
        # Shrunk output can be seen thanks to the maxdiff property.
        self.maxDiff = None

        # first Object
        idty = self.obj_1.id
        attributes = {}
        attributes['created_at'] = self.obj_1.created_at
        attributes['updated_at'] = self.obj_1.updated_at
        expected_output = f'[MakeupStyle] ({idty}) {attributes}\n'

        # StringIO creates a mock file to capture text
        captured = StringIO()

        # since standard output is a file, I replaced the stdot file
        # with the mock file from StringIO
        sys.stdout = captured

        print(self.obj_1)
        output = captured.getvalue()

        # return the stdout file
        sys.stdout = sys.__stdout__
        self.assertEqual(expected_output, output)


        # Second Object
        idty = self.obj_2.id
        attributes = {}
        attributes['name'] = self.obj_2.name
        attributes['created_at'] = self.obj_2.created_at
        attributes['updated_at'] = self.obj_2.updated_at

        expected_output = f'[MakeupStyle] ({idty}) {attributes}\n'

        # StringIO creates a mock file to capture text
        captured = StringIO()

        # since standard output is a file, I replaced the stdot file
        # with the mock file from StringIO
        sys.stdout = captured

        print(self.obj_2)
        output = captured.getvalue()

        # return the stdout file
        sys.stdout = sys.__stdout__
        self.assertEqual(expected_output, output)


        # third Object
        idty = self.obj_3.id
        attributes = {}
        attributes['name'] = self.obj_3.name
        attributes['created_at'] = self.obj_3.created_at
        attributes['updated_at'] = self.obj_3.updated_at
        expected_output = f'[MakeupStyle] ({idty}) {attributes}\n'

        # StringIO creates a mock file to capture text
        captured = StringIO()

        # since standard output is a file, I replaced the stdot file
        # with the mock file from StringIO
        sys.stdout = captured

        print(self.obj_3)
        output = captured.getvalue()

        # return the stdout file
        sys.stdout = sys.__stdout__
        self.assertEqual(expected_output, output)


    def test_make_json(self):
        """Tests the function to create a dictionary of the object.
        """
        json_rep = self.obj_3.make_json()
        self.assertIsInstance(json_rep, dict)
        self.assertIn('__class__', json_rep.keys())
        self.assertIn('id', json_rep.keys())
        self.assertIn('name', json_rep.keys())
        self.assertIn('created_at', json_rep.keys())
        self.assertIn('updated_at', json_rep.keys())
        
