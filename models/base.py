from abc import ABC
from typing import Dict

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
        saved_data = DATABASE_CONNECTION.insert(self.__class__.__name__, data)

        self.__dict__.update(saved_data)

    def update(self):
        """
        Updates an existing object in the database
        :return: None
        """
        data = self.serialize()

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

    def __str__(self):
        return f'{self.__class__.__name__}({self.id})'

    def __repr__(self):
        return self.__str__()
