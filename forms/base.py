import json
from abc import abstractmethod

import stringcase

from models.base import Model
from utils import prompt_enter, clear, input_list


class Form:
    BOLD_COLOR = '\033[1m'
    COLOR_END = '\033[0m'

    def __init__(self, model: Model):
        self.model = model

    @abstractmethod
    def get_fields(self):
        """
        Returns a list of fields required in the form
        :return: List
        """

    def pre_save(self):
        pass

    def post_save(self):
        pass

    def render(self):
        """
        Function to render the input form
        and capture the input data
        :return: Dict
        """
        clear()

        fields = self.get_fields()

        data = {}

        for field in fields:
            if field['type'] == 'list':
                print(f'Enter {self.BOLD_COLOR}{stringcase.pascalcase(field["name"])}{self.COLOR_END}')
                data[field['name']] = input_list()
            else:
                data[field['name']] = input(f'Enter {self.BOLD_COLOR}'
                                            f'{stringcase.pascalcase(field["name"])}{self.COLOR_END}')

        print('\nDetails Entered: ')

        print(json.dumps(data, indent=2))

        print('\n')

        prompt_enter()
