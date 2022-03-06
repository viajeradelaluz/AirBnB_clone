#!/usr/bin/python3
""" Module with Unittest for the User class.
    """
import inspect
import unittest

from models.user import User


class TestBaseModel(unittest.TestCase):
    """ Testing the User class of the program.
        """

    @classmethod
    def setUp(cls):
        """ Method to prepare each single test.
            """
        cls.user_test = User()
        cls.user_test.email = "foo@bar.com"
        cls.user_test.password = "FooBar1234"
        cls.user_test.first_name = "Foo"
        cls.user_test.last_name = "Bar"

    def test_module_documentation(self):
        """ Test if User module is documented.
            """
        self.assertTrue(User.__doc__)

    def test_class_documentation(self):
        """ Test if User class is documented.
            """
        self.assertTrue(User.__doc__)

    def test_methods_documentation(self):
        """ Test if all User methods are documented.
            """
        methods = inspect.getmembers(User)
        for method in methods:
            self.assertTrue(inspect.getdoc(method))

    def test_basic_base_assigment(self):
        """ Create some basic User instances.
            """
        self.assertIsInstance(self.user_test, User)
        self.assertTrue(hasattr(self.user_test, "id"))
        self.assertTrue(hasattr(self.user_test, "created_at"))
        self.assertTrue(hasattr(self.user_test, "updated_at"))

    def test_base_assigment_attributes(self):
        """ Test User instance assigment attributes.
            """
        self.assertTrue(hasattr(self.user_test, "email"))
        self.assertEqual(self.user_test.email, "foo@bar.com")
        self.assertTrue(hasattr(self.user_test, "password"))
        self.assertEqual(self.user_test.password, "FooBar1234")
        self.assertTrue(hasattr(self.user_test, "first_name"))
        self.assertEqual(self.user_test.first_name, "Foo")
        self.assertTrue(hasattr(self.user_test, "last_name"))
        self.assertEqual(self.user_test.last_name, "Bar")

    def test_to_dict_method(self):
        """ Check the to_dict() method.
            """
        user_as_dict = self.user_test.to_dict()
        self.assertIsInstance(user_as_dict, dict)
        self.assertEqual(self.user_test.id, user_as_dict["id"])

    def test_str_method(self):
        """ Check the __str__() method.
            """
        user_fstr = "[{}] ({}) {}".format(self.user_test.__class__.__name__,
                                          self.user_test.id,
                                          self.user_test.__dict__)
        user_str = self.user_test.__str__()
        self.assertEqual(user_fstr, user_str)
