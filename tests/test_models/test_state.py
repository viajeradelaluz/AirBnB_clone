#!/usr/bin/python3
""" Module with Unittest for the State class.
    """
import inspect
import json
import os
import unittest
import uuid

from models.state import State


class TestBaseModel(unittest.TestCase):
    """ Testing the State class of the program.
        """

    def setUp(self):
        """ Method to prepare each single test.
            """
        self.b = State()
        self.b.save()

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
        self.assertIsInstance(self.b, State)
        self.assertTrue(hasattr(self.b, "id"))
        self.assertTrue(hasattr(self.b, "created_at"))
        self.assertTrue(hasattr(self.b, "updated_at"))

    def test_base_id_assigment(self):
        """ Test if the id of the instance is UUID v4.
            """
        uuid_v4 = uuid.UUID(self.b.id, version=4)
        self.assertEqual(str(uuid_v4), self.b.id)

    def test_base_assigment_arguments(self):
        """ Test State instance assigment with arguments.
            """
        b = State(15)
        b.name = "I'm a State"
        self.assertTrue(hasattr(b, "name"))
        self.assertEqual(b.to_dict()["name"], "I'm a State")
        self.assertFalse(hasattr(b, "15"))

    def test_save_method(self):
        """ Check the save() method.
            """
        b_save = State()
        b_save.save()
        self.assertTrue(os.path.exists("file.json"))
        with open("file.json") as file_opened:
            file_dict = json.load(file_opened)
        self.assertTrue(b_save.to_dict() in file_dict.values())

    def test_to_dict_method(self):
        """ Check the to_dict() method.
            """
        obj_as_dict = self.b.to_dict()
        self.assertEqual(self.b.id, obj_as_dict["id"])

    def test_str_method(self):
        """ Check the __str__() method.
            """
        b_srt_string = "[{}] ({}) {}".format(self.b.__class__.__name__,
                                             self.b.id, self.b.__dict__)
        b_srt = self.b.__str__()
        self.assertEqual(b_srt_string, b_srt)
