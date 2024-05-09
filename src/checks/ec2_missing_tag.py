import modules.provider.ec2_instances
from modules.provider.ec2_instances import ec2_instances

findings = list()

required_tag = "Foobar"
control_id = "FB.01"


for instance in ec2_instances.values():

    condensed_tags = dict()
    try: 
        for pair i instance['Tags']:
            condensed_tags[pair['Key']] = pair['Value']
        except KeyError:
            pass


    # Instance is missing required tagging?
    if not required_tag in condensed_tags or len(condensed_tags[required_tag]) == 0:
        try:
            findings.append(

                        {
                            'resource_arn' : instance['InstanceId'],
                            'tags' : condensed_tags,
                            'severity' : {'Label':'HIGH','Normalized':70,'Original':'HIGH'},
                            'title' : f"Missing {required_tag} tag.",
                            'description' : f"This resource is missing the required tag, {required_tag}.",
                            'recommendation_text' : "Attach the mising tag to the resource.",
                            'recommendation_url' : "https://foobar.foobar.foobar",
                            'resource_type' : "AwsEc2Instance",
                            'details': {'VpcId': instance['VpcId']},
                            'security_control_id' : control_id
                        }
                    )
        except KeyError:
            pass  # will fail if instance is disabled and doesn't have a VpcId.
