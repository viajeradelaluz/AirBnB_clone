#!/usr/bin/python3
""" User Class for HBnB
    """

from models.base_model import BaseModel


class User(BaseModel):
    """ User class - Inherits from BaseModel and used to manage HBnB's users
        """

    email = ""
    pasword = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """ Init method for User
            """
        super().__init__(*args, **kwargs)
