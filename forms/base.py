import json
from abc import abstractmethod
from typing import Dict

import stringcase

from api import UserLogin
from exceptions import ValidationError
from models.base import Model
from utils import prompt_enter, clear, input_list


class Form:
    BOLD_COLOR = '\033[1m'
    COLOR_END = '\033[0m'

    @abstractmethod
    def show_banner(self):
        pass

    @abstractmethod
    def get_fields(self):
        """
        Returns a list of fields required in the form
        :return: List
        """

    def validate(self, data):
        logged_in_user = UserLogin.check_session()

        if not logged_in_user:
            raise ValidationError(
                message='Please login first.'
            )

    def save(self, data: Dict):
        pass

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
        self.show_banner()

        admin_check = getattr(self, 'only_admin', None)

        if admin_check:
            UserLogin.admin_check()

        fields = self.get_fields()

        data = {}

        for field in fields:
            if field['type'] == 'list':
                print(f'Enter {self.BOLD_COLOR}{stringcase.pascalcase(field["name"])}{self.COLOR_END}')
                if field.get('supporting_text'):
                    print(f'({field["supporting_text"]})')
                data[field['name']] = input_list()
            else:
                print(f'Enter {self.BOLD_COLOR}{stringcase.pascalcase(field["name"])}{self.COLOR_END}')
                if field.get('supporting_text'):
                    print(f'({field["supporting_text"]})')
                data[field['name']] = input()

        print('\nDetails Entered: ')

        print(json.dumps(data, indent=2))

        print('\n')

        prompt_enter()

        self.pre_save()
        self.save(data)
        self.post_save()
