from os import system, name

from .singleton import DatabaseSingleton


def prompt_enter():
    input("Press ENTER to continue..")


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
