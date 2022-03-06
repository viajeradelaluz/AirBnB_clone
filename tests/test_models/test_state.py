#!/usr/bin/python3
""" Module with Unittest for the State class.
    """
import inspect
import json
import os
import unittest

from models.state import State


class TestState(unittest.TestCase):
    """ Testing the State class of the program.
        """

    def setUp(self):
        """ Method to prepare each single test.
            """
        self.state_test = State()
        self.state_test.name = "Cundinamarca"
        if os.path.exists("file.json"):
            os.rename("file.json", "original_file.json")

    def test_module_documentation(self):
        """ Test if State module is documented.
            """
        self.assertTrue(State.__doc__)

    def test_class_documentation(self):
        """ Test if State class is documented.
            """
        self.assertTrue(State.__doc__)

    def test_methods_documentation(self):
        """ Test if all State methods are documented.
            """
        methods = inspect.getmembers(State)
        for method in methods:
            self.assertTrue(inspect.getdoc(method))

    def test_basic_base_assigment(self):
        """ Create some basic State instances.
            """
        self.assertIsInstance(self.state_test, State)
        self.assertTrue(hasattr(self.state_test, "id"))
        self.assertTrue(hasattr(self.state_test, "created_at"))
        self.assertTrue(hasattr(self.state_test, "updated_at"))

    def test_base_assigment_arguments(self):
        """ Test State instance assigment with arguments.
            """
        self.assertTrue(hasattr(self.state_test, "name"))
        self.assertEqual(self.state_test.to_dict()["name"], "Cundinamarca")

    def test_save_method(self):
        """ Check the save() method.
            """
        self.state_test.save()
        self.assertTrue(os.path.exists("file.json"))
        with open("file.json") as file_opened:
            file_dict = json.load(file_opened)
        self.assertTrue(self.state_test.to_dict() in file_dict.values())

    def test_to_dict_method(self):
        """ Check the to_dict() method.
            """
        obj_as_dict = self.state_test.to_dict()
        self.assertEqual(self.state_test.id, obj_as_dict["id"])

    def test_str_method(self):
        """ Check the __str__() method.
            """
        state_fstr = "[{}] ({}) {}".format(self.state_test.__class__.__name__,
                                           self.state_test.id,
                                           self.state_test.__dict__)
        state_srt = self.state_test.__str__()
        self.assertEqual(state_fstr, state_srt)

    def tearDown(self):
        """ Method to leave each test
            """
        if os.path.exists("file.json"):
            os.remove("file.json")
        if os.path.exists("original_file.json"):
            os.rename("original_file.json", "file.json")
