from typing import Dict
from utils import Singleton


class MemoryDatabase(Singleton):
    def __init__(self):
        self.data = {}

    def save(self, model: str, record: Dict):
        index = self.data[model].size() + 1

        record['id'] = index
        self.data[model].append(record)
