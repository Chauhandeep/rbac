from forms.base import Form
from models import Resource


class ResourceForm(Form):
    def __init__(self):
        super(ResourceForm, self).__init__(
            model=Resource
        )

    def get_fields(self):
        return [
            {
                'name': 'name',
                'type': 'string'
            }
        ]
