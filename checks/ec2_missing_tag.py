import modules.provider.ec2_instances
from modules.provider.ec2_instances import ec2_instances

required_tag = "Foobar"
control_id = "FB.01"


for instance in ec2_instances:
    # Instance is missing required tagging?
    if not required_tag in instance.Tags or if len(instance.Tags[required_tag]) == 0:
        try:
            findings.append(

                        {
                            resource_arn = instance['InstanceId'],
                            tags = instance['Tags'],
                            severity = {'Label':'HIGH','Normalized':70,'Original':'HIGH'},
                            title = f"Missing {required_tag} tag.",
                            description = f"This resource is missing the required tag, {required_tag}.",
                            recommendation_text = "Attach the mising tag to the resource.",
                            recommendation_url = "https://foobar.foobar.foobar"
                            resource_type = "AwsEc2Instance",
                            details: {'VpcId': instance['VpcId']},
                            security_control_id = control_id
                        }
                    )
        except KeyError:
            pass  # will fail if instance is disabled and doesn't have a VpcId.
