from typing import Dict

from forms.base import Form
from models import Role


class RoleForm(Form):
    def __init__(self):
        super(RoleForm, self).__init__()

    def show_banner(self):
        print('########################################')
        print('           Role REGISTRATION            ')
        print('########################################')
        print('\n\n')

    def save(self, data: Dict):
        role = Role(data)
        role.save()

    def get_fields(self):
        return [
            {
                'name': 'name',
                'type': 'string'
            },
            {
                'name': 'policies',
                'type': 'list',
                'supporting_text': 'Enter policy ids to be added'
            }
        ]
