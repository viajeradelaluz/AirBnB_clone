#!/usr/bin/python3
""" Module with Unittest for the FileStorage class.
    """
import inspect
import unittest

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ Testing the FileStorage class of the program.
        """

    def setUp(self):
        """ Method to prepare each single test.
            """
        self.storage_test = FileStorage()

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
        self.assertIsInstance(self.storage_test, FileStorage)

    def test_save_method(self):
        """ Check the save() method.
            """
        base_model_test = BaseModel()
        self.storage_test.new(base_model_test)
        self.storage_test.save()
        self.assertTrue(self.storage_test._FileStorage__file_path)
        self.assertTrue(self.storage_test._FileStorage__objects)
        self.assertFalse(hasattr(self.storage_test, "__file_path"))
        self.assertFalse(hasattr(self.storage_test, "__objects"))

    def test_reload_method(self):
        """ Check the reload() method.
            """
        base_model_test = BaseModel()
        self.storage_test.new(base_model_test)
        self.storage_test.save()
        key_to_search = "BaseModel.{}".format(base_model_test.id)
        self.storage_test.reload()
        file_dict = self.storage_test.all()
        self.assertTrue(key_to_search in file_dict.keys())
