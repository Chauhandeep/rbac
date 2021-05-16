from abc import ABC
from typing import Dict
from db import MemoryDatabase


class Model(ABC):
    def __init__(self):
        self.database_connection = MemoryDatabase()

    def save(self, record: Dict):
        """
        Saves an object to the database
        :param record: Row to be inserted
        :return: None
        """
        self.database_connection.insert(self.__class__.__name__, record)

    def update(self, old_instance, new_record: Dict):
        """
        Updates an existing object in the database
        :param old_instance: old instance to be updated
        :param new_record: new record to be inserted
        :return: None
        """
        new_record['id'] = old_instance.id

        self.database_connection.update(self.__class__.__name__, old_instance.id, new_record)

    def delete(self, instance):
        """
        Deletes an object from the database
        :param instance: Instance to be deleted
        :return: None
        """
        self.database_connection.delete(self.__class__.__name__, instance.id)
