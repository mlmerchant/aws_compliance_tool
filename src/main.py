from modules.config.read_config import read_config
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


print(len(findings))
