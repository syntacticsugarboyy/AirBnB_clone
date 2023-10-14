#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
    BaseModel
'''
from datetime import datetime
import uuid
import models


class BaseModel:
    '''
        Base Model for other classes
    '''
    def __init__(self, *args, **kwargs):
        if (kwargs):
            for key, value in kwargs.items():
                if key == 'creates_at':
                    value = datetime.fromisoformat(value)
                    self.created_at = value
                elif key == 'updated_at':
                    value = datetime.fromisoformat(value)
                    self.updated_at = value
                elif key == 'id':
                    self.id = str(value)
        else:
            self.id = uuid.uuid4()
            self.created_at = datetime.now().isoformat()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        '''
            Displays a string representation of the instance
        '''
        name = type(self).__name__
        return ('[{}] ({}) {}'.format(name, self.id, self.__dict__))

    def save(self):
        '''
            Updates updated_at with current datetime
        '''
        self.updated_at = datetime.now().isoformat()
        models.storage.save()

    def to_dict(self):
        '''
            Returns a dictionary format containing attributes of the object
        '''
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = type(self).__name__
        dictionary['created_at'] = self.created_at
        dictionary['updated_at'] = self.updated_at

        return dictionary
