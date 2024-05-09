from modules.config.read_config import read_config
from modules.findings.write_findings import write_finding
import os
import importlib


# application settings
configuration = read_config(file_path='./config.ini')


# if needed, create the results folder
results_folder = configuration['RESULTS']['folder']
if not os.path.exists(results_folder):
    os.makedirs(results_folder)


findings = list()


# iterate through the checks
checks = list(configuration['CHECKS'].keys())
for check in checks:
    module = importlib.import_module(check)
    findings.extend(module.findings)


# push the findings to ndjson formated file
for finding in findings:
    write_finding(
        **finding,
        product_name   = configuration['ORGANIZATION']['product_name'],
        product_arn    = configuration['ORGANIZATION']['product_arn'],
        company_name   = configuration['ORGANIZATION']['company_name'],
        results_folder = configuration['RESULTS']['folder']
            )
