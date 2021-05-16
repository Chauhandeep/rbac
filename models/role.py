from typing import Dict

from exceptions import ValidationError
from models import Policy
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

        policies = data.get('policies')

        policy_objs = Policy.get(filters={'id': policies})

        if len(policies) != len(policy_objs):
            raise ValidationError(
                message=f'Failed to add policies to role.\n'
                        f'Few policy id seems to be invalid.'
            )
