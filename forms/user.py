from forms.base import Form
from models import User


class UserForm(Form):
    def __init__(self):
        super(UserForm, self).__init__(
            model=User
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
            }
        ]
