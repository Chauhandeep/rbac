from typing import Dict

from forms.base import Form
from api.login import UserLogin


class LoginForm(Form):
    def __init__(self):
        super(LoginForm, self).__init__()

    def show_banner(self):
        print('########################################')
        print('              USER LOGIN                ')
        print('########################################')
        print('\n\n')

    def render(self):
        session = UserLogin.check_session()

        if session:
            print(f'You are logged in as {session.username}!')
            return

        super(LoginForm, self).render()

    def save(self, data: Dict):
        if not UserLogin.login(username=data['username'], password=data['password']):
            print('Invalid Username or password. Please try again.')
        else:
            print('Login Successful!')

    def get_fields(self):
        return [
            {
                'name': 'username',
                'type': 'string'
            },
            {
                'name': 'password',
                'type': 'string'
            }
        ]
