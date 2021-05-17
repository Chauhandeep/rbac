from os import system, name

from .singleton import DatabaseSingleton


def prompt_enter(message = None):
    if message is None:
        message = "Press ENTER to continue.."
    input(message)


def prompt_choice():
    try:
        choice = int(input("\nPlease enter your choice\n"))
        return choice
    except ValueError:
        print("Invalid Input\n\n")
        return prompt_choice()


def input_list():
    print('Enter # to stop.')

    data = []
    while True:
        ch = input()

        if ch == '#':
            break

        data.append(ch)

    return data


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
