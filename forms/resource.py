from typing import Dict

from exceptions import ValidationError
from forms.base import Form
from models import Resource


class ResourceForm(Form):
    def __init__(self):
        super(ResourceForm, self).__init__()

        self.only_admin = True

    def show_banner(self):
        print('########################################')
        print('         RESOURCE REGISTRATION          ')
        print('########################################')
        print('\n\n')

    def save(self, data: Dict):
        self.validate(data)

        try:
            resource = Resource(data)
            resource.save()
        except ValueError as err:
            raise ValidationError(
                message=str(err)
            )

    def get_fields(self):
        return [
            {
                'name': 'name',
                'type': 'string'
            }
        ]
