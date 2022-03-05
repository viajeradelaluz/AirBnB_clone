#!/usr/bin/python3
""" Module with Unittest for the User class.
    """
import inspect
import unittest

from models.user import User


class TestBaseModel(unittest.TestCase):
    """ Testing the User class of the program.
        """

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
        user = User()
        self.assertIsInstance(user, User)
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))

    def test_base_assigment_attributes(self):
        """ Test User instance assigment attributes.
            """
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertEqual(user.email, "")
        self.assertTrue(hasattr(user, "password"))
        self.assertEqual(user.password, "")
        self.assertTrue(hasattr(user, "first_name"))
        self.assertEqual(user.first_name, "")
        self.assertTrue(hasattr(user, "last_name"))
        self.assertEqual(user.last_name, "")

    def test_to_dict_method(self):
        """ Check the to_dict() method.
            """
        user = User()
        user_as_dict = user.to_dict()
        self.assertIsInstance(user_as_dict, dict)
        self.assertEqual(user.id, user_as_dict["id"])

    def test_str_method(self):
        """ Check the __str__() method.
            """
        user = User()
        user_fstr = "[{}] ({}) {}".format(user.__class__.__name__,
                                         user.id, user.__dict__)
        user_str = user.__str__()
        self.assertEqual(user_fstr, user_str)
