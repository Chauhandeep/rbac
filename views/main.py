from api import UserLogin
from models import User, Resource, Policy, Role
from views.base import View
from forms import *


class MainView(View):
    def prepare_view(self):
        self.add_choice(
            text='Login',
            trigger=LoginForm().render
        )

        self.add_choice(
            text='Logout',
            trigger=UserLogin.logout
        )

        self.add_choice(
            text='Add Resource',
            trigger=ResourceForm().render
        )

        self.add_choice(
            text='View All Resources',
            trigger=Resource.display
        )

        self.add_choice(
            text='Add Policy',
            trigger=PolicyForm().render
        )

        self.add_choice(
            text='View All Policies',
            trigger=Policy.display
        )

        self.add_choice(
            text='Add Role',
            trigger=RoleForm().render
        )

        self.add_choice(
            text='View All Roles',
            trigger=Role.display
        )

        self.add_choice(
            text='Add User',
            trigger=UserForm().render
        )

        self.add_choice(
            text='View All Users',
            trigger=User.display
        )

        self.add_choice(
            text='Exit',
            trigger=exit
        )
