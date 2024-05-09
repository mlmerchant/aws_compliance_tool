from modules.config.read_config import read_config
import os


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
    from check import findings as new_findings:
        findings.extend(new_findings)


print(len(findings))
