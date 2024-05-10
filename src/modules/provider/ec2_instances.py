import boto3


# populate global dict of all ec2 instances using instance id as key
def populate() -> dict:
    resource = dict() 
    ec2_client = boto3.client('ec2')
    reservations = ec2_client.describe_instances()['Reservations']
    for reservation in reservations:
        for instance in reservation['Instances']:
            resource[instance['InstanceId']] = instance
    return resource

                            
