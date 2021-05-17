from typing import Dict

from exceptions import ValidationError
from forms.base import Form
from models import Policy, User


class PolicyForm(Form):
    def __init__(self):
        super(PolicyForm, self).__init__()
        self.only_admin = True

    def show_banner(self):
        print('########################################')
        print('         POLICY REGISTRATION            ')
        print('########################################')
        print('\n\n')

    def save(self, data: Dict):
        try:
            action = data['action']
            data['action'] = int(action) if '1' <= action <= '6' else action

            policy = Policy(data)
            policy.save()
        except ValueError as err:
            raise ValidationError(
                message=str(err)
            )

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
                'supporting_text': 'Enter 1=>GET, 2=>WRITE, 3=>DELETE, 4=>PUT, 5=>PATCH, 6=>HEAD, ALL=>*'
            },
            {
                'name': 'resource',
                'type': 'string'
            }
        ]
