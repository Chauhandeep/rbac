from typing import Dict

from models.base import Model


class Session(Model):
    def __init__(self, details: Dict):
        super(Session, self).__init__(
            id_=details.get('id')
        )

        self.username = details['username']
        self.full_name = details['full_name']
