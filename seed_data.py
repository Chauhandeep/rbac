from models import *


def add_admin_user():
    iam_resource = Resource(
        {
            'name': 'iam'
        }
    )
    iam_resource.save()

    admin_policy = Policy(
        {
            'name': 'AdminPolicy',
            'effect': 'allow',
            'action': '*',
            'resource': '*'
        }
    )

    admin_policy.save()

    admin_role = Role(
        {
            'name': 'Admin Role',
            'policies': [1]
        }
    )

    admin_role.save()

    admin_user = User(
        {
            'username': 'admin',
            'password': 'admin',
            'full_name': 'Deepanshu Chauhan',
            'roles': [1]
        }
    )

    admin_user.save()


def add_resources():
    res = Resource(
        {
            'name': 'S3'
        }
    )
    res.save()

    res = Resource(
        {
            'name': 'EC2'
        }
    )
    res.save()

    res = Resource(
        {
            'name': 'ApiGateway'
        }
    )
    res.save()


def add_policies():
    pol = Policy(
        {
            'name': 'S3FullAccess',
            'effect': 'allow',
            'resource': 'S3',
            'action': '*'
        }
    )
    pol.save()

    pol = Policy(
        {
            'name': 'S3ReadAccess',
            'effect': 'allow',
            'resource': 'S3',
            'action': 1
        }
    )
    pol.save()

    pol = Policy(
        {
            'name': 'EC2FullAccess',
            'effect': 'allow',
            'resource': 'EC2',
            'action': '*'
        }
    )
    pol.save()

    pol = Policy(
        {
            'name': 'EC2ReadAccess',
            'effect': 'allow',
            'resource': 'EC2',
            'action': 1
        }
    )
    pol.save()

    pol = Policy(
        {
            'name': 'ApiGatewayFullAccess',
            'effect': 'allow',
            'resource': 'ApiGateway',
            'action': '*'
        }
    )
    pol.save()

    pol = Policy(
        {
            'name': 'ApiGatewayReadAccess',
            'effect': 'allow',
            'resource': 'ApiGateway',
            'action': 1
        }
    )
    pol.save()


def add_roles():
    role_ = Role(
        {
            'name': 'QA',
            'policies': [
                3, 5, 7
            ]
        }
    )

    role_.save()

    role_ = Role(
        {
            'name': 'developer',
            'policies': [
                2, 4, 6
            ]
        }
    )

    role_.save()


def add_users():
    qa = User({
        'username': 'qa',
        'password': 'qa',
        'full_name': 'QA User',
        'roles': [2]
    })
    qa.save()

    developer = User({
        'username': 'developer',
        'password': 'developer',
        'full_name': 'Developer User',
        'roles': [3]
    })
    developer.save()


def initialize_seed_data():
    add_admin_user()
    add_resources()
    add_policies()
    add_roles()
    add_users()
