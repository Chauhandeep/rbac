from exceptions import ValidationError
from models import User, Resource, Role, Policy
from models.actions import ActionTypes

from api.login import UserLogin


class AccessControl:
    @staticmethod
    def check(action: ActionTypes, resource: Resource):
        """
        Function to check the user access for a particular action on resource
        :return: bool
        """
        logged_in_user = User.get(
            filters={
                'username': UserLogin.check_session().username
            })[0]

        user_roles = Role.get(filters={
            'id': logged_in_user.roles
        })

        policies = []
        for role in user_roles:
            policies.extend(role.policies)

        user_policies = Policy.get(
            filters={
                'id': policies
            }
        )

        resource_policies = [
            policy for policy in user_policies if policy.resource == '*' or policy.resource == resource
        ]

        # check for the denied policy
        denied_policy = next(
            (
                policy for policy in resource_policies
                if policy.effect == 'deny' and (policy.action == '*' or policy.action == action)
            ),
            None
        )

        if denied_policy:
            return False

        # check for an allowed policy
        allowed_policy = next(
            (
                policy for policy in resource_policies
                if policy.effect == 'allow' and (policy.action == '*' or policy.action == action)
            ),
            None
        )

        if allowed_policy:
            return True

        return False
