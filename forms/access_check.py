from typing import Dict

from api import UserLogin, AccessControl
from exceptions import ValidationError
from forms.base import Form
from models import Resource
from models.actions import ActionTypes


class AccessCheckForm(Form):
    def __init__(self):
        super(AccessCheckForm, self).__init__()

    def show_banner(self):
        print('########################################')
        print('             ACCESS CHECK               ')
        print('########################################')
        print('\n\n')

    def render(self):
        logged_in_user = UserLogin.check_session()

        if not logged_in_user:
            raise ValidationError(
                message='Please login first.'
            )

        super(AccessCheckForm, self).render()

    def validate(self, data):
        try:
            action = data['action']
            resource = data['resource']

            if int(action) not in [action.value for action in ActionTypes]:
                raise ValidationError(
                    message='Invalid action type'
                )

            resources = Resource.get(filters={
                'name': [resource]
            })

            if len(resources) == 0:
                raise ValidationError(
                    message=f'Resource {resource} not found'
                )
        except ValueError as err:
            raise ValidationError(message=f'Invalid Input - {str(err)}')

    def save(self, data: Dict):
        self.validate(data)

        if AccessControl.check(int(data['action']), data['resource']):
            print("[+] Access Granted!!")
        else:
            print("[-] Access Denied")

    def get_fields(self):
        return [
            {
                'name': 'action',
                'type': 'string',
                'supporting_text': 'Enter 1=>GET, 2=>WRITE, 2=>DELETE, 4=>PUT, 5=>PATCH, 6=>HEAD'
            },
            {
                'name': 'resource',
                'type': 'string',
                'supporting_text': 'Enter Resource name'
            }
        ]
