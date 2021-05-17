class CustomException(Exception):
    def __init__(self, message=None):
        if message is None:
            self.message = 'Internal Error'
        else:
            self.message = message

    def __str__(self):
        return f'{self.__repr__()}: {self.message}'


class ObjectDoesNotExist(CustomException):
    def __init__(self):
        super(ObjectDoesNotExist, self).__init__(
            message='Record not found in the database'
        )


class RelationDoesNotExist(CustomException):
    def __init__(self, message):
        super(RelationDoesNotExist, self).__init__(
            message=message
        )


class IntegrityError(CustomException):
    def __init__(self, message):
        super(IntegrityError, self).__init__(
            message=message
        )


class ValidationError(CustomException):
    def __init__(self, message):
        super(ValidationError, self).__init__(
            message=message
        )


class UserNotLoggedIn(CustomException):
    def __init__(self, message=None):
        if message is None:
            message = 'User Not Logged In'
        super(UserNotLoggedIn, self).__init__(
            message=message
        )
