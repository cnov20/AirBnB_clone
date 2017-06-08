#!/usr/bin/python3
""" Base model """

from datetime import datetime, date, time
from uuid import uuid4
import json
from models import storage

class BaseModel:
    """ defining BaseModel class """
    def __init__(self, *args, **kwargs):
        if len(args) > 0 and type(args[0]) is dict:
            if 'id' in kwargs:
                self.id = kwargs.get('id')
            if 'created_at' in kwargs:
                self.created_at = datetime.strptime(kwargs.get('created_at'), "%Y-%m-%d %H:%M:%S.%f")
            if 'updated_at' in kwargs:
                self.updated_at = datetime.strptime(kwargs.get('updated_at'), "%Y-%m-%d %H:%M:%S.%f")
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def to_json(self):
        newDict = self.__dict__.copy()
        newDict.update({'__class__': self.__class__.__name__})
        newDict.update({'created_at': str(self.created_at)})
        newDict.update({'updated_at': str(self.updated_at)})
        return (newDict)

    def __str__(self):
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                 self.id, self.__dict__))