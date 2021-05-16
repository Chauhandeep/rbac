from typing import Dict

from models.base import Model


class Resource(Model):
    def __init__(self, data: Dict):
        super(Resource, self).__init__(
            id_=data.get('id')
        )

        self.name = data['name']
