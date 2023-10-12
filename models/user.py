#!/usr/bin/python3

"""This is the user module inherited from basemodel"""

from models.base_model import BaseModel


class User(BaseModel):
    """The public class attributes of string-empty string"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
