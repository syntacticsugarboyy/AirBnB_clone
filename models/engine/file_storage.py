#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
    Store First Object
'''
from json import dumps, loads
from os.path import isfile
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    '''
        Serializes and Deserializes JSON files to instances.
    '''
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        '''
            Returns the dictionary __objects
        '''
        return (FileStorage.__objects)

    def new(self, obj):
        '''
            Sets in __objects the obj with key <obj class name>.id
        '''
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        '''
            Serializes __objects to __path
        '''
        dict_f = {
                key: value.to_dict()
                for key, value in FileStorage.__objects.items()}
        json_str = dumps(dict_f)
        filename = FileStorage.__file_path
        with open(filename, 'w') as f:
            f.write(json_str)

    def reload(self):
        '''
            Deserializes the JSON file to __objects
        '''
        allowed_class = ['BaseModel', 'User', 'State', 'City', 'Amenity',
                        'Place', 'Review']
        filename = FileStorage.__file_path
        if isfile(filename):
            with open(filename, 'r') as f:
                json_str = f.read()
                dict_f = loads(json_str)
            for key, value in dicti_f.items():
                class_name, obj_id = key.split('.')
                if class_name in allowed_class:
                    eval('self.new({}(**value))'.format(class_name))
