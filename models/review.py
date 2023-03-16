#!/usr/bin/python3
"""module containing a Review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Class containing  review objects"""

    place_id = ""
    user_id = ""
    text = ""
