#!/usr/bin/python3
""" this module containes the review class """


from models.base_model import BaseModel


class Review(BaseModel):
    """ this is the reveiw class """

    place_id = ""
    user_id = ""
    text = ""
