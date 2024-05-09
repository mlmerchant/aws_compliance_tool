import boto3

instance_profiles = dict()

def get_instance_profiles() -> None:
  # creates map of instance profile arn to profile details
  paginator = iam_client.get_paginator('list_instance_profiles')
  for page in paginator.paginate():
    for profile in page['InstanceProfiles']:
      instance_profiles[profile['Arn']] = profile
