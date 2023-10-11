#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
    BaseModel
'''
from datetime import datetime
from uuid import uuid
import models


class BaseModel:
    '''
        Base Model for other classes
    '''
    self.id = uuid4()
    self.created_at = datetime.now()
    self.updated_at = self.created_at.isoformat()

    def __str__(self):
        '''
            Displays a string representation of the instance
        '''
        name = type(self).__name__
        print('[{}] ({}) {}'.format(name, self.id, self.__dict__))

    def save(self):
        '''
            Updates updated_at with current datetime
        '''
        self.updated_at = datetime.now().isoformat()

    def to_dict(self):
        '''
            Returns a dictionary format containing attributes of the object
        '''
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = type(self).__name__
        dictionary['created_at'] = self.created_at
        dictionary['updated_at'] = self.updated_at

        return dictionary
