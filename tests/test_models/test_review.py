#!/usr/bin/python3
""" Module with Unittest for the Review class.
    """
import inspect
import json
import os
import unittest

from models.review import Review


class TestBaseModel(unittest.TestCase):
    """ Testing the Review class of the program.
        """

    @classmethod
    def setUp(cls):
        """ Method to prepare each single test.
            """
        cls.review_test = Review()
        cls.review_test.place_id = "5698"
        cls.review_test.user_id = "1542"
        cls.review_test.text = "Arctic Fox Igloos is a luxurious\
                                glass igloo resort"

    def test_module_documentation(self):
        """ Test if Review module is documented.
            """
        self.assertTrue(Review.__doc__)

    def test_class_documentation(self):
        """ Test if Review class is documented.
            """
        self.assertTrue(Review.__doc__)

    def test_methods_documentation(self):
        """ Test if all Review methods are documented.
            """
        methods = inspect.getmembers(Review)
        for method in methods:
            self.assertTrue(inspect.getdoc(method))

    def test_basic_base_assigment(self):
        """ Create some basic Review instances.
            """
        self.assertIsInstance(self.review_test, Review)
        self.assertTrue(hasattr(self.review_test, "id"))
        self.assertTrue(hasattr(self.review_test, "created_at"))
        self.assertTrue(hasattr(self.review_test, "updated_at"))

    def test_base_assigment_attributes(self):
        """ Test Review instance assigment attributes.
            """
        self.assertTrue(hasattr(self.review_test, "place_id"))
        self.assertTrue(hasattr(self.review_test, "user_id"))
        self.assertTrue(hasattr(self.review_test, "text"))

        self.assertIsInstance(self.review_test.place_id, str)
        self.assertIsInstance(self.review_test.user_id, str)
        self.assertIsInstance(self.review_test.text, str)

    def test_save_method(self):
        """ Check the save() method.
            """
        self.review_test.save()
        self.assertTrue(os.path.exists("file.json"))
        with open("file.json") as file_opened:
            file_dict = json.load(file_opened)
        self.assertTrue(self.review_test.to_dict() in file_dict.values())

    def test_to_dict_method(self):
        """ Check the to_dict() method.
            """
        obj_as_dict = self.review_test.to_dict()
        self.assertEqual(self.review_test.id, obj_as_dict["id"])

    def test_str_method(self):
        """ Check the __str__() method.
            """
        rew_fstr = "[{}] ({}) {}".format(self.review_test.__class__.__name__,
                                         self.review_test.id,
                                         self.review_test.__dict__)
        rew_str = self.review_test.__str__()
        self.assertEqual(rew_fstr, rew_str)
