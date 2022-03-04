#!/usr/bin/python3
""" Test for base model class
    """


import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """ Test class for basemodel
        """


    def setUp(self):
        kwargs = {"id": 1}
        self.instance = BaseModel()
        self.instance_from_kwargs = BaseModel(**kwargs)

    