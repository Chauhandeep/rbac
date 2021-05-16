from typing import Dict

from models.base import Model


class Role(Model):
    def __init__(self, data: Dict):
        super(Role, self).__init__(
            id_=data.get('id')
        )

        self.name = data['name']
        self.policies = data['policies']

    def validate(self, data: Dict):
        super(Role, self).validate(data)
