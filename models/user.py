from typing import Dict

from exceptions import ValidationError
from models.role import Role
from models.base import Model


class User(Model):
    def __init__(self, details: Dict):
        super(User, self).__init__(
            id_=details.get('id')
        )

        self.username = details['username']
        self.password = details['password']
        self.full_name = details['full_name']

        self.roles = [int(id_) for id_ in details['roles']]

    def validate(self, data: Dict):
        super(User, self).validate(data)

        username = data['username']

        obj = User.get(filters={
            'username': [username]
        })

        if len(obj) > 0:
            raise ValidationError(
                message=f'user with username {username} already exists!'
            )

        roles = data.get('roles')

        role_objs = Role.get(filters={'id': roles})

        if len(roles) != len(role_objs):
            raise ValidationError(
                message=f'Failed to add roles to the user.\n'
                        f'Few role id seems to be invalid.'
            )
        
    def __str__(self):
        data = self.__dict__
        
        data.pop('password')
        return super(User, self).__str__()
