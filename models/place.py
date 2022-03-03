#!/usr/bin/python3
""" Place class for HBnB
    """

from models.base_model import BaseModel


class Place(BaseModel):
    """ Place class for HBnB. Inherits from BaseModel
        """

    city_id = ""
    user_id = ""
    name = ""
    descriptio = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0.0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """ Init method for place
            """
        super().__init__(*args, **kwargs)
