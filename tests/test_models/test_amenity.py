#!/usr/bin/python3
""" Module with Unittest for the Amenity class.
    """
import inspect
import json
import os
import unittest

from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """ Testing the Amenity class of the program.
        """

    @classmethod
    def setUp(cls):
        """ Method to prepare each single test.
            """
        cls.amenity_test = Amenity()
        cls.amenity_test.name = "Wi-fi"
        if os.path.exists("file.json"):
            os.rename("file.json", "original_file.json")

    def test_module_documentation(self):
        """ Test if Amenity module is documented.
            """
        self.assertTrue(Amenity.__doc__)

    def test_class_documentation(self):
        """ Test if Amenity class is documented.
            """
        self.assertTrue(Amenity.__doc__)

    def test_methods_documentation(self):
        """ Test if all Amenity methods are documented.
            """
        methods = inspect.getmembers(Amenity)
        for method in methods:
            self.assertTrue(inspect.getdoc(method))

    def test_basic_base_assigment(self):
        """ Create some basic Amenity instances.
            """
        self.assertIsInstance(self.amenity_test, Amenity)
        self.assertTrue(hasattr(self.amenity_test, "id"))
        self.assertTrue(hasattr(self.amenity_test, "created_at"))
        self.assertTrue(hasattr(self.amenity_test, "updated_at"))

    def test_base_assigment_attributes(self):
        """ Test Amenity instance assigment attributes.
            """
        self.assertTrue(hasattr(self.amenity_test, "name"))
        self.assertEqual(self.amenity_test.name, "Wi-fi")

    def test_save_method(self):
        """ Check the save() method.
            """
        self.amenity_test.save()
        self.assertTrue(os.path.exists("file.json"))
        with open("file.json") as file_opened:
            file_dict = json.load(file_opened)
        self.assertTrue(self.amenity_test.to_dict() in file_dict.values())

    def test_to_dict_method(self):
        """ Check the to_dict() method.
            """
        obj_as_dict = self.amenity_test.to_dict()
        self.assertEqual(self.amenity_test.id, obj_as_dict["id"])

    def test_str_method(self):
        """ Check the __str__() method.
            """
        amnt_fstr = "[{}] ({}) {}".format(self.amenity_test.__class__.__name__,
                                          self.amenity_test.id,
                                          self.amenity_test.__dict__)
        amenity_str = self.amenity_test.__str__()
        self.assertEqual(amnt_fstr, amenity_str)

    def tearDown(self):
        """ Method to leave each test
            """
        if os.path.exists("file.json"):
            os.remove("file.json")
        if os.path.exists("original_file.json"):
            os.rename("original_file.json", "file.json")
