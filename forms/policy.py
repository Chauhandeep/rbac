from forms.base import Form
from models import Policy


class PolicyForm(Form):
    def __init__(self):
        super(PolicyForm, self).__init__(
            model=Policy
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
                'type': 'string'
            },
            {
                'name': 'resource',
                'type': 'string'
            }
        ]
