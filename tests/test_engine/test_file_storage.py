#!/usr/bin/python3
""" Module with Unittest for the FileStorage class.
    """
import inspect
import json
import os
import unittest
import uuid

from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    """ Testing the FileStorage class of the program.
        """

    def setUp(self):
        """ Method to prepare each single test.
            """
        self.b = FileStorage()
        self.b.save()

    def test_module_documentation(self):
        """ Test if FileStorage module is documented.
            """
        self.assertTrue(FileStorage.__doc__)

    def test_class_documentation(self):
        """ Test if FileStorage class is documented.
            """
        self.assertTrue(FileStorage.__doc__)

    def test_methods_documentation(self):
        """ Test if all FileStorage methods are documented.
            """
        methods = inspect.getmembers(FileStorage)
        for method in methods:
            self.assertTrue(inspect.getdoc(method))

    def test_basic_base_assigment(self):
        """ Create some basic FileStorage instances.
            """
        self.assertIsInstance(self.b, FileStorage)

    def test_save_method(self):
        """ Check the save() method.
            """
        b1 = FileStorage()
        self.b.new(b1)
        self.b.save()
        self.assertTrue(self.b.__file_path)
        self.assertTrue(self.b.__objects)

    def test_reload_method(self):
        """ Check the reload() method.
            """
        pass
