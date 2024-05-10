import boto3


    f"arn:{parition}:ec2:{region}:{account_id}:instance/{resource_id}"



# populate global dict of all ec2 instances using instance id as key
def populate() -> dict:
    resource = dict() 
    ec2_client = boto3.client('ec2')
    reservations = ec2_client.describe_instances()['Reservations']
    for reservation in reservations:
        for instance in reservation['Instances']:

            try:
                # Attempt to enrich with resource arn for EC2 Instances
                #TODO - determine region without relying on private dns, which may not be enabled
                resource_id = instance['InstanceId']
                ip_arn = instance['IamInstanceProfile']['Arn'].split(':')
                parition = ip_arn[1]
                account_id = ip_arn[4]
                region = ["NetworkInterfaces"][0]["PrivateDnsName"].split('.')[1]
                instance['Arn'] = f"arn:{parition}:ec2:{region}:{account_id}:instance/{resource_id}"
            except KeyError:
                pass


            resource[instance['InstanceId']] = instance
    return resource

                            
