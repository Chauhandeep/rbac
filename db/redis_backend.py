from typing import Dict

import stringcase

from db.backend import DatabaseBackend
from exceptions import ObjectDoesNotExist, RelationDoesNotExist, IntegrityError


class RedisDatabase(DatabaseBackend):
    def __init__(self):
        self.data = {}

    @staticmethod
    def get_table_name_from_model(model: str):
        raise NotImplementedError()

    def insert(self, model: str, record: Dict):
        raise NotImplementedError()

    def delete(self, model: str, id_: int):
        raise NotImplementedError()

    def update(self, model: str, id_: int, record: Dict):
        raise NotImplementedError()

    def get(self, model: str):
        raise NotImplementedError()
