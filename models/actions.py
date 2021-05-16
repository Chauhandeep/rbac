import enum


class ActionTypes(enum.Enum):
    GET = 1
    WRITE = 2
    DELETE = 3
    PUT = 4
    PATCH = 5
    HEAD = 6
    ALL = '*'
