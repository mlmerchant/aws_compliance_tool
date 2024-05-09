import boto3

roles = dict()

get_iam_roles() -> None:
paginator = iam_client.get_paginator('list_roles')
for page in paginator.paginate():
    for role in page['Roles']:
        roles[role['RoleName']] = role
