from typing import Dict

from forms.base import Form
from models import User


class UserForm(Form):
    def __init__(self):
        super(UserForm, self).__init__()

    def show_banner(self):
        print('########################################')
        print('           USER REGISTRATION            ')
        print('########################################')
        print('\n\n')

    def save(self, data: Dict):
        user = User(data)
        user.save()

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
