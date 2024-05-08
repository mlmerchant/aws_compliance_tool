def map_instance_profile_to_roles() -> dict:
    # Mapping of all instance profile to role_arn
    # 
    # Returnsdictionary of instance profile to attached roles.
    #

    instance_profile_to_role = dict()

    for profile in instance_profiles:
        try:
            instance_profile_to_role[profile['Arn'] = profile['Roles'][0]['Arn']
        except IndexError:
            continue
    return instance_profile_to_role

def verify_role(role: str, policy_arn: str) -> bool:
    # Returns True ifthe policy arn of interest is attached.
    #
    # Input role name and policy arn of interest.
    #
    #
    ## TODO, get single map of attached policies to roles
