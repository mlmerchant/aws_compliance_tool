import boto3

def populate() -> dict:
    # Create a boto3 EC2 client
    ec2_client = boto3.client('ec2')

    # Initialize a paginator for describe_security_groups
    paginator = ec2_client.get_paginator('describe_security_groups')

    # Initialize an empty dictionary to store security groups
    security_groups_dict = {}

    for page in paginator.paginate():
        for sg in page['SecurityGroups']:
            # Use the security group ID as the key and the security group object as the value
            sg_id = sg['GroupId']
            security_groups_dict[sg_id] = sg

    return security_groups_dict

