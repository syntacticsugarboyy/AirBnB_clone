#!/usr/bin/python3

"""This is the review module inherited from the basemodel"""

from models.base_model import BaseModel


class Review(BaseModel):
    """The public class attribute of string-empty string"""
    place_id = ""
    user_id = ""
    text = ""
