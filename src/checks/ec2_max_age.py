from datetime import datetime

requirements = ['modules.provider.ec2_instances']



def run_check(resources: dict) -> list:
    
    max_age_in_days = 365
    control_id = "foobar.02"


    ec2_instances = resources['ec2_instances']
    findings = list()


    
    today = datetime.now().replace(tzinfo=None)


    for instance in ec2_instances.values():
        
        launch_time = instance['LaunchTime']
        delta = today - launch_time
        age = delta.days


        # Instance is missing required tagging?
        if age >= max_age_in_days:
            try:
                findings.append(

                            {
                                'resource_arn' : instance['Arn'],
                                'tags' : condensed_tags,
                                'severity' : {'Label':'CRITICAL','Normalized':100,'Original':'CRITICAL'},
                                'title' : f"Missing {required_tag} tag.",
                                'description' : f"This resource is older than {str(max_age_in_days)}.",
                                'recommendation_text' : "Delete this resource, and if required, recreate this resource from an approved baseline.",
                                'recommendation_url' : "https://foobar.foobar.foobar",
                                'resource_type' : "AwsEc2Instance",
                                'details': {'VpcId': instance['VpcId']},
                                'security_control_id' : control_id
                            }
                        )
            except KeyError:
                pass  # will fail if instance is disabled and doesn't have a VpcId.

    return findings
