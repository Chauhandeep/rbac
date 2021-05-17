from typing import Dict

from exceptions import ValidationError
from forms.base import Form
from models import User


class UserForm(Form):
    def __init__(self):
        super(UserForm, self).__init__()

        self.only_admin = True

    def show_banner(self):
        print('########################################')
        print('           USER REGISTRATION            ')
        print('########################################')
        print('\n\n')

    def save(self, data: Dict):
        self.validate(data)

        try:
            user = User(data)
            user.save()
        except ValueError as err:
            raise ValidationError(
                message=str(err)
            )

    def get_fields(self):
        return [
            {
                'name': 'username',
                'type': 'string'
            },
            {
                'name': 'password',
                'type': 'string'
            },
            {
                'name': 'full_name',
                'type': 'string'
            },
            {
                'name': 'roles',
                'type': 'list',
                'supporting_text': 'Enter role ids to be added'
            }
        ]
