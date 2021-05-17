from abc import abstractmethod
from typing import Dict

from exceptions import CustomException
from utils import prompt_choice, clear, prompt_enter


class View:
    def __init__(self):
        self.choices = list()

    @classmethod
    def show_banner(cls):
        print('########################################')
        print('#   ROLE BASED ACCESS CONTROL SYSTEM   #')
        print('########################################')
        print('\n\n')

    def add_choice(self, text: str, trigger):
        """
        Function to add choice in a view
        :param text: Main Text
        :param trigger: Trigger when this choice is selected
        :return: None
        """
        self.choices.append({
            'text': text,
            'trigger': trigger
        })

    @staticmethod
    def print_choice(index: int, choice: Dict):
        """
        Function to print the choice
        :param index: int
        :param choice: Dict
        :return:
        """
        print(f'{index} => {choice["text"]}')

    @abstractmethod
    def prepare_view(self):
        pass

    def render(self):
        """
        Function to render the view
        :return: None
        """
        try:
            clear()

            self.show_banner()

            index = 0
            for choice in self.choices:
                index += 1
                self.print_choice(index, choice)

            while True:
                choice = prompt_choice()

                if 0 < choice <= index:
                    break
                else:
                    print("Invalid Choice.\n")

            self.choices[choice-1]['trigger']()
        except CustomException as exc:
            print(f'\033[91m{exc.message}\033[0m')

        prompt_enter(message='Press ENTER to return to main menu.')
        self.render()
