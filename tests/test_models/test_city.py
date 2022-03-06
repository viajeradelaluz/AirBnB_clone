#!/usr/bin/python3
""" Module with Unittest for the City class.
    """
import inspect
import json
import os
import unittest

from models.city import City


class TestBaseModel(unittest.TestCase):
    """ Testing the City class of the program.
        """

    @classmethod
    def setUp(cls):
        """ Method to prepare each single test.
            """
        cls.city_test = City()
        cls.city_test.state_id = "22"
        cls.city_test.name = "Kyiv"

    def test_module_documentation(self):
        """ Test if City module is documented.
            """
        self.assertTrue(City.__doc__)

    def test_class_documentation(self):
        """ Test if City class is documented.
            """
        self.assertTrue(City.__doc__)

    def test_methods_documentation(self):
        """ Test if all City methods are documented.
            """
        methods = inspect.getmembers(City)
        for method in methods:
            self.assertTrue(inspect.getdoc(method))

    def test_basic_base_assigment(self):
        """ Create some basic City instances.
            """
        self.assertIsInstance(self.city_test, City)
        self.assertTrue(hasattr(self.city_test, "id"))
        self.assertTrue(hasattr(self.city_test, "created_at"))
        self.assertTrue(hasattr(self.city_test, "updated_at"))

    def test_base_assigment_attributes(self):
        """ Test City instance assigment with attributes.
            """
        self.assertTrue(hasattr(self.city_test, "state_id"))
        self.assertEqual(self.city_test.to_dict()["state_id"], "22")
        self.assertTrue(hasattr(self.city_test, "name"))
        self.assertEqual(self.city_test.to_dict()["name"], "Kyiv")

    def test_save_method(self):
        """ Check the save() method.
            """
        self.city_test.save()
        self.assertTrue(os.path.exists("file.json"))
        with open("file.json") as file_opened:
            file_dict = json.load(file_opened)
        self.assertTrue(self.city_test.to_dict() in file_dict.values())

    def test_to_dict_method(self):
        """ Check the to_dict() method.
            """
        obj_as_dict = self.city_test.to_dict()
        self.assertEqual(self.city_test.id, obj_as_dict["id"])

    def test_str_method(self):
        """ Check the __str__() method.
            """
        city_fstr = "[{}] ({}) {}".format(self.city_test.__class__.__name__,
                                          self.city_test.id,
                                          self.city_test.__dict__)
        city_str = self.city_test.__str__()
        self.assertEqual(city_fstr, city_str)
