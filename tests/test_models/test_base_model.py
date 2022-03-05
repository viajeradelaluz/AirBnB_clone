#!/usr/bin/python3
""" Module with Unittest for the BaseModel class.
    """
import inspect
import os
import unittest
import uuid

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ Testing the BaseModel class of the program.
        """

    def setUp(self):
        """ Method to prepare each single test
            """
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_module_documentation(self):
        """ Test if BaseModel module is documented.
            """
        self.assertTrue(BaseModel.__doc__)

    def test_class_documentation(self):
        """ Test if BaseModel class is documented.
            """
        self.assertTrue(BaseModel.__doc__)

    def test_methods_documentation(self):
        """ Test if all BaseModel methods are documented.
            """
        methods = inspect.getmembers(BaseModel)
        for method in methods:
            self.assertTrue(inspect.getdoc(method))

    def test_basic_base_assigment(self):
        """ Create some basic BaseModel instances.
            """
        b = BaseModel()
        self.assertIsInstance(b, BaseModel)
        self.assertTrue(hasattr(b, "id"))
        self.assertTrue(hasattr(b, "created_at"))
        self.assertTrue(hasattr(b, "updated_at"))

    def test_base_id_assigment(self):
        """ Test if the id of the instance is UUID v4.
            """
        b = BaseModel()
        uuid_v4 = uuid.UUID(b.id, version=4)
        self.assertEqual(str(uuid_v4), b.id)

    def test_base_assigment_arguments(self):
        """ Test BaseModel instance assigment with arguments.
            """
        b = BaseModel(15)
        b.name = "I'm a BaseModel"
        self.assertTrue(hasattr(b, "name"))
        self.assertEqual(b.to_dict()["name"], "I'm a BaseModel")
        self.assertFalse(hasattr(b, "15"))
