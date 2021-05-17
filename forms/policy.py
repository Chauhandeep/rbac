from typing import Dict

from forms.base import Form
from models import Policy, User


class PolicyForm(Form):
    def __init__(self):
        super(PolicyForm, self).__init__(
            model=Policy
        )

    def show_banner(self):
        print('########################################')
        print('         POLICY REGISTRATION            ')
        print('########################################')
        print('\n\n')

    def save(self, data: Dict):
        policy = Policy(data)
        policy.save()

    def get_fields(self):
        return [
            {
                'name': 'name',
                'type': 'string'
            },
            {
                'name': 'effect',
                'type': 'string'
            },
            {
                'name': 'action',
                'type': 'string',
                'supporting_text': 'Enter 1=>GET, 2=>WRITE, 2=>DELETE, 4=>PUT, 5=>PATCH, 6=>HEAD, ALL=>*'
            },
            {
                'name': 'resource',
                'type': 'string'
            }
        ]
