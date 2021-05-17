from typing import Dict

from forms.base import Form
from models import Resource


class ResourceForm(Form):
    def __init__(self):
        super(ResourceForm, self).__init__()

    def show_banner(self):
        print('########################################')
        print('         RESOURCE REGISTRATION          ')
        print('########################################')
        print('\n\n')

    def save(self, data: Dict):
        resource = Resource(data)
        resource.save()

    def get_fields(self):
        return [
            {
                'name': 'name',
                'type': 'string'
            }
        ]
