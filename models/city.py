#!/usr/bin/python3

"""This is the city module inherited from the BaseModel
"""

from models.base_model import BaseModel


class City(BaseModel):
    """The public attribute for string-empty string"""
    state_id = ""
    name = ""
