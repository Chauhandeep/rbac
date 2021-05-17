from exceptions import UserNotLoggedIn, ValidationError
from models import User, Session


class UserLogin:
    @staticmethod
    def check_session():
        session = Session.get()

        if len(session) > 0:
            return session[0]

        return None

    @staticmethod
    def login(username: str, password: str):
        """
        Function to authenticate a user
        :return: bool
        """
        users = User.get(filters={
            'username': [username],
            'password': [password]
        })

        if len(users) == 0:
            return False

        user = users[0]
        UserLogin.save_session(user)

        return True

    @staticmethod
    def save_session(user: User):
        session = Session(
            user.serialize()
        )

        session.save()

    @staticmethod
    def logout():
        session = Session.get()

        if len(session) == 0:
            raise UserNotLoggedIn()

        session = session[0]
        session.delete()

        print(f'{session.username} Logged out.')

    @staticmethod
    def admin_check():
        session = UserLogin.check_session()

        if session is None:
            raise ValidationError(
                message='Please log in first.'
            )

        logged_in_user = User.get(
            filters={
                'username': UserLogin.check_session().username
            })[0]

        if logged_in_user.username != 'admin':
            raise ValidationError(
                message='Access Forbidden. You need to be an administrator to use this functionality.'
            )
