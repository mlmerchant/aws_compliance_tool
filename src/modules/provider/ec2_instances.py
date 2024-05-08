import boto3

ec2_instances = dict()

def get_ec2_instances() -> None:
  # populate global dict of all ec2 instances using instance id as key
  ec2_client = boto3.client('ec2')
  reservations = ec2_client.describe_instances()['Reservations']
  for reservation in reservations:
    for instance in reservation['Instances']:
      ec2_instances[instance['InstanceId']] = instance


                            
