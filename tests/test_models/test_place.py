#!/usr/bin/python3
""" Module with Unittest for the Place class.
    """
import inspect
import json
import os
import unittest

from models.place import Place


class TestPlace(unittest.TestCase):
    """ Testing the Place class of the program.
        """

    @classmethod
    def setUp(cls):
        """ Method to prepare each single test.
            """
        cls.place_test = Place()
        cls.place_test.city_id = "22"
        cls.place_test.user_id = "1542"
        cls.place_test.name = "Igloo 12"
        cls.place_test.description = "Arctic Fox Igloss"
        cls.place_test.number_rooms = 3
        cls.place_test.number_bathrooms = 1
        cls.place_test.max_guest = 4
        cls.place_test.price_by_night = 45
        cls.place_test.latitude = 71.7069
        cls.place_test.longitude = 42.6043
        cls.place_test.amenity_ids = ["Lakeside location", "Own kitchenette"
                                      "Private Sauna", "Sky Panorama View"]
        if os.path.exists("file.json"):
            os.rename("file.json", "original_file.json")

    def test_module_documentation(self):
        """ Test if Place module is documented.
            """
        self.assertTrue(Place.__doc__)

    def test_class_documentation(self):
        """ Test if Place class is documented.
            """
        self.assertTrue(Place.__doc__)

    def test_methods_documentation(self):
        """ Test if all Place methods are documented.
            """
        methods = inspect.getmembers(Place)
        for method in methods:
            self.assertTrue(inspect.getdoc(method))

    def test_basic_base_assigment(self):
        """ Create some basic Place instances.
            """
        self.assertIsInstance(self.place_test, Place)
        self.assertTrue(hasattr(self.place_test, "id"))
        self.assertTrue(hasattr(self.place_test, "created_at"))
        self.assertTrue(hasattr(self.place_test, "updated_at"))

    def test_base_assigment_attributes(self):
        """ Test Place instance assigment with attributes
            """
        self.assertTrue(hasattr(self.place_test, "city_id"))
        self.assertTrue(hasattr(self.place_test, "user_id"))
        self.assertTrue(hasattr(self.place_test, "name"))
        self.assertTrue(hasattr(self.place_test, "description"))
        self.assertTrue(hasattr(self.place_test, "number_rooms"))
        self.assertTrue(hasattr(self.place_test, "max_guest"))
        self.assertTrue(hasattr(self.place_test, "price_by_night"))
        self.assertTrue(hasattr(self.place_test, "latitude"))
        self.assertTrue(hasattr(self.place_test, "longitude"))
        self.assertTrue(hasattr(self.place_test, "amenity_ids"))

        self.assertIsInstance(self.place_test.city_id, str)
        self.assertIsInstance(self.place_test.user_id, str)
        self.assertIsInstance(self.place_test.name, str)
        self.assertIsInstance(self.place_test.description, str)
        self.assertIsInstance(self.place_test.number_rooms, int)
        self.assertIsInstance(self.place_test.number_bathrooms, int)
        self.assertIsInstance(self.place_test.max_guest, int)
        self.assertIsInstance(self.place_test.price_by_night, int)
        self.assertIsInstance(self.place_test.latitude, float)
        self.assertIsInstance(self.place_test.longitude, float)
        self.assertIsInstance(self.place_test.amenity_ids, list)

    def test_save_method(self):
        """ Check the save() method.
            """
        self.place_test.save()
        self.assertTrue(os.path.exists("file.json"))
        with open("file.json") as file_opened:
            file_dict = json.load(file_opened)
        self.assertTrue(self.place_test.to_dict() in file_dict.values())

    def test_to_dict_method(self):
        """ Check the to_dict() method.
            """
        obj_as_dict = self.place_test.to_dict()
        self.assertEqual(self.place_test.id, obj_as_dict["id"])

    def test_str_method(self):
        """ Check the __str__() method.
            """
        place_fstr = "[{}] ({}) {}".format(self.place_test.__class__.__name__,
                                           self.place_test.id,
                                           self.place_test.__dict__)
        place_str = self.place_test.__str__()
        self.assertEqual(place_fstr, place_str)

    def tearDown(self):
        """ Method to leave each test
            """
        if os.path.exists("file.json"):
            os.remove("file.json")
        if os.path.exists("original_file.json"):
            os.rename("original_file.json", "file.json")
