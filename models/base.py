import json
from abc import ABC
from typing import Dict

from exceptions import ValidationError
from settings import DATABASE_CONNECTION


class Model(ABC):
    def __init__(self, id_: int = None):
        self.id = id_

    def serialize(self):
        """
        Method to serialize instance into database record
        :return: Dict
        """
        data = {}

        for k, v in self.__dict__.items():
            if not k.startswith('__'):
                data[k] = v

        return data

    @classmethod
    def deserialize(cls, row: Dict):
        """
        Method to deserialize database record into instance
        :return: Model Object
        """
        return cls(row)

    def save(self):
        """
        Saves an object to the database
        :return: None
        """
        data = self.serialize()

        self.validate(data)

        saved_data = DATABASE_CONNECTION.insert(self.__class__.__name__, data)

        self.__dict__.update(saved_data)

    def update(self):
        """
        Updates an existing object in the database
        :return: None
        """
        data = self.serialize()

        self.validate(data)

        saved_data = DATABASE_CONNECTION.update(self.__class__.__name__, data['id'], data)

        self.__dict__.update(saved_data)

    def delete(self):
        """
        Deletes an object from the database
        :return: None
        """
        DATABASE_CONNECTION.delete(self.__class__.__name__, self.id)

    @classmethod
    def get(cls, filters: Dict = None):
        """
        Function to return all users based on a filter
        :param filters: Dict
        :return: User
        """
        if filters is None:
            filters = {}

        data = DATABASE_CONNECTION.get(cls.__name__)

        for k, v in filters.items():
            data = [row for row in data if row[k] in v]

        res = [cls.deserialize(row) for row in data]

        return res

    def validate(self, data: Dict):
        """
        Function to validate the data before saving into the database
        :param data:
        :return: bool
        """
        for key in self.__dict__.keys():
            if not key.startswith('__') and key != 'id':
                if data[key] == '' or data[key] is None:
                    raise ValidationError(
                        message=f'{key} should not be "{data[key]}"'
                    )

    def __str__(self):
        return json.dumps(self.__dict__, indent=2)

    def __repr__(self):
        return self.__str__()
