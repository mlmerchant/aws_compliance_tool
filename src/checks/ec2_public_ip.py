requirements = ['modules.provider.ec2_instances']


def run_check(resources: dict) -> list:
    
    control_id = "foobar.03"


    ec2_instances = resources['ec2_instances']
    findings = list()


    for instance in ec2_instances.values():
        

        condensed_tags = dict()
        try: 
            for pair in instance['Tags']:
                condensed_tags[pair['Key']] = pair['Value']
        except KeyError:
            pass
        

        # Instance has public ip address?
        if 'PublicIpAddress' in instance:
            try:
                findings.append(

                            {
                                'resource_arn' : instance['Arn'],
                                'tags' : condensed_tags,
                                'severity' : {'Label':'CRITICAL','Normalized':100,'Original':'CRITICAL'},
                                'title' : f"Instance has a public IP address.",
                                'description' : f"Ingress traffic to an EC2 instance should not occur directly.",
                                'recommendation_text' : "Do not place EC2 instances in public subnets.  Ensure traffic to an EC2 instances first transits through a load balancer with attached web applicable firewall.",
                                'recommendation_url' : "https://foobar.foobar.foobar",
                                'resource_type' : "AwsEc2Instance",
                                'details': {'VpcId': instance['VpcId']},
                                'security_control_id' : control_id
                            }
                        )
            except KeyError:
                pass  # will fail if instance is disabled and doesn't have a VpcId.

    return findings

