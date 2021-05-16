from typing import Dict

from models.base import Model


class User(Model):
    def __init__(self, details: Dict):
        super(User, self).__init__(
            id_=details.get('id')
        )

        self.username = details['username']
        self.password = details['password']
        self.full_name = details['full_name']
