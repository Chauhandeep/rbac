from typing import Dict

import stringcase

from db.backend import DatabaseBackend
from exceptions import ObjectDoesNotExist, RelationDoesNotExist


class MemoryDatabase(DatabaseBackend):
    def __init__(self):
        self.data = {}

    @staticmethod
    def get_table_name_from_model(model: str):
        return stringcase.snakecase(model)

    def insert(self, model: str, record: Dict):
        """
        Inserts a record into the table
        :param model: model name
        :param record: row to be inserted
        :return: None
        """

        table_name = self.get_table_name_from_model(model)

        if table_name not in self.data.keys():
            self.data[table_name] = list()

        index = record.get('id', len(self.data[model]) + 1)

        record['id'] = index
        self.data[model].append(record)

    def delete(self, model: str, id_: int):
        """
        Deletes a record from a table
        :param model: model name
        :param id_: id of the record to be deleted
        :return: None
        """

        try:
            table_name = self.get_table_name_from_model(model)

            index = -1

            for i in range(0, len(self.data[model])):
                if self.data[model][i]['id'] == id_:
                    index = i

            if index == -1:
                raise ObjectDoesNotExist()

            self.data[model].pop(index)
        except KeyError:
            raise RelationDoesNotExist(
                message=f'Relation {table_name} does not exists in the database'
            )

    def update(self, model: str, id_: int, record: Dict):
        """
        Updates a record in a table
        :param model: model name
        :param id_: id of thr row to be deleted
        :param record: new data to be updated
        :return: None
        """

        self.delete(model, id_)

        record['id'] = id_

        self.insert(model, record)

    def get_data(self):
        return self.data
