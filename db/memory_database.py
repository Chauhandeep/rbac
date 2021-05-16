from typing import Dict

import stringcase

from db.backend import DatabaseBackend
from exceptions import ObjectDoesNotExist, RelationDoesNotExist, IntegrityError


class MemoryDatabase(DatabaseBackend):
    def __init__(self):
        self.data = {}

    @staticmethod
    def get_table_name_from_model(model: str):
        return stringcase.snakecase(model)

    def insert(self, model: str, record: Dict):
        table_name = self.get_table_name_from_model(model)

        if table_name not in self.data.keys():
            self.data[table_name] = list()

        id_ = record.get('id', len(self.data[table_name]) + 1) or len(self.data[table_name]) + 1

        existing_row = None

        if id_ <= len(self.data[table_name]):
            existing_row = next((row for row in self.data[table_name] if row['id'] == id_), None)

        if existing_row:
            raise IntegrityError(
                message=f'Row with id ({id_}) exists in table {table_name}'
            )

        record['id'] = id_
        self.data[table_name].append(record)

        return record

    def delete(self, model: str, id_: int):
        try:
            table_name = self.get_table_name_from_model(model)

            index = -1

            for i in range(0, len(self.data[table_name])):
                if self.data[table_name][i]['id'] == id_:
                    index = i

            if index == -1:
                raise ObjectDoesNotExist()

            print(f'Deleting index {index}')
            self.data[table_name].pop(index)
        except KeyError:
            raise RelationDoesNotExist(
                message=f'Relation {table_name} does not exists in the database'
            )

    def update(self, model: str, id_: int, record: Dict):
        self.delete(model, id_)

        self.insert(model, record)

        return record

    def get(self, model: str):
        table_name = self.get_table_name_from_model(model)

        if table_name not in self.data.keys():
            self.data[table_name] = list()

        return self.data[table_name]
