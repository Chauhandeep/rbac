from forms.base import Form
from models import Role


class RoleForm(Form):
    def __init__(self):
        super(RoleForm, self).__init__(
            model=Role
        )

    def get_fields(self):
        return [
            {
                'name': 'name',
                'type': 'string'
            },
            {
                'name': 'policies',
                'type': 'list'
            }
        ]
