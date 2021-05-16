from abc import ABC, abstractmethod
from typing import Dict

from utils import DatabaseSingleton


class DatabaseBackend(DatabaseSingleton, ABC):
    @abstractmethod
    def insert(self, model: str, record: Dict):
        """
        Inserts a record into the table
        :param model: model name
        :param record: row to be inserted
        :return: None
        """
        pass

    @abstractmethod
    def delete(self, model: str, id_: int):
        """
        Deletes a record from a table
        :param model: model name
        :param id_: id of the record to be deleted
        :return: None
        """
        pass

    @abstractmethod
    def update(self, model: str, id_: int, record: Dict):
        """
        Updates a record in a table
        :param model: model name
        :param id_: id of thr row to be deleted
        :param record: new data to be updated
        :return: None
        """
        pass
