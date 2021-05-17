from exceptions import UserNotLoggedIn
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
