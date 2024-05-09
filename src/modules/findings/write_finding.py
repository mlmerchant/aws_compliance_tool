import json
import modules.findings.finding_id
from datetime import datetime

def write_finding(
    resource_arn: str,
    tags: dict,
    severity: dict,
    title: str,
    description: str,
    recommendation_text: str,
    resource_type: str,
    details: dict,
    security_control_id: dict,
    company_name: str,
    product_name: str,
    product_arn: str,
    results_folder: str,
    recommendation_url: str=""
) -> None:
   
    # Constants
    SCHEMA_VERSION = '2018-10-08'
    TYPES = [f"{product_name} Checks"]

    finding_arn = generate_finding_arn(product_name, resource_arn, security_control_id)

    finding_hash = finding_arn.split('/')[-1]
    aws_account = resource_arn.split(':')[4]
    region = resource_arn.split(':')[3]
    

    now = datetime.now()
    iso_date = now.strftime("%Y-%m-%d")

    finding = {
      'SchemaVersion': SCHEMA_VERSION,
      'Id': finding_arn,
      'ProductArn': product_arn,
      'ProductName': product_name,
      'CompanyName': company_name,
      'Region': region,
      'GeneratorId': security_control_id,
      'AwsAccountId': aws_account,
      'Types': TYPES,
      'LastObservedAt': f"{iso_date}T00:00:00.000Z",
      'CreatedAt': f"{iso_date}T00:00:00.000Z",
      'Severity': severity,
      'Title': title,
      'Description': description,
      'Remedation': {'Recommendation':{'Text': recommendation_text, 'Url': recommendation_url}},
      'Resources': [
        {
          'Tags': tags,
          'Type': resource_type
          'id' resource_arn
          'Region': region,
          'Details': {
            resource_type: details,
          }
        }
      ]

      with open(results_folder + '/' +  finding_hash + '.ndjson', 'w') as f:
          json.dump(finding, f, seperators=(',',':'))
        
      return None

