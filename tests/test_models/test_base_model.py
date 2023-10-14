#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
    BaseModel Tests
'''
import unittest
from datetime import datetime
from uuid import UUID
# import patch?

class TestBaseModel(unittest.TestCase):
    '''
        BaseModel Tests
    '''
    def test_moduleDocs(self):
        '''
            Tests the module import
        '''
        module_doc = __import__('models.base_model').base_model.__doc__
        self.assertGreater(len(module_doc), 0)

    def test_classDocs(self):
        '''
            Tests the import classes
        '''
        class_doc = __import__('models.base_model').base_model.BaseModel.__doc__
        self.assertGreater(len(class_doc), 0)

    def test_methodDocSave(self):
        '''
            Test methods viability
        '''
        methodDoc = (
                __import__('models.base_model')
                .base_model.BaseModel.__str__.__doc__)
        self.assertGreater(len(methodDoc), 0)

    def test_idType(self):
        '''
        '''
        instance = BaseModel()
        self.assertIs(type(instance.id), str)

    def test_idLength(self):
        '''
            Tests the Length of an id
        '''
        idlen = BaseModel()
        self.assertEqual(len(idlen.id), 36)

    def test_idValidity(self):
        '''
            Tests for the Validity of an id
        '''
        idvalid = BaseModel()
        self.assertIs(type(UUID(idvalid.id)), UUID)

    def test_created_atType(self):
        '''
            Checks of the created_at attribute is a valid datetime
        '''
        create_date = BaseModel()
        self.assertIs(type(create_date.created_at), datetime)

    def test_updated_atType(self):
        '''
            Checks of the created_at attribute is a valid datetime
        '''
        update_date = BaseModel()
        self.assertIs(type(update_date.updated_at), datetime)

    def test___str__output(self):
        '''
            Checks the output of __str__
        '''
        obj = BaseModel()
        self.assertEqual((f'[BaseModel] ({obj.id}) {obj.__dict__}'), str(obj))
