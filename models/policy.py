from typing import Dict

from exceptions import ValidationError
from models.resource import Resource
from models.actions import ActionTypes
from models.base import Model


class Policy(Model):
    def __init__(self, data: Dict):
        super(Policy, self).__init__(
            id_=data.get('id')
        )

        self.name = data['name']
        self.version = 'v1'
        self.effect = data['effect']
        self.action = data['action']
        self.resource = data['resource']

    def validate(self, data: Dict):
        super(Policy, self).validate(data)

        effect = data.get('effect')
        action = data.get('action')
        resource = data.get('resource')

        if effect not in ['allow', 'deny']:
            raise ValidationError(
                message=f'unsupported effect "{effect}"'
            )

        if action != '*' and int(action) not in [action.value for action in ActionTypes]:
            raise ValidationError(
                message=f'unsupported action "{action}"'
            )

        if resource != '*':
            resource_obj = next(
                (resource for resource in Resource.get(filters={'name': [resource]})),
                None
            )

            if not resource_obj:
                raise ValidationError(
                    message=f'Resource Not Found "{resource}"'
                )
