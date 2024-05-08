import boto3
import modules.provider.iam_roles as iam_roles

# Policy name to list of attached roles
role_to_polices = dict()

for role in iam_roles.roles:
    role_to_policies[role] = iam_client.list_attached_policies(RoleName=role)['AttachedPolicies']
     
    
