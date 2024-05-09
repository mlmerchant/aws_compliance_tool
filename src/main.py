from modules.config.read_config import read_config
import os


# application settings
configuration = read_config(file_path='./config.ini')


# if needed, create the results folder
results_folder = configuration['RESULTS']['folder']
if not os.path.exists(results_folder):
    os.makdirs(results_folder)



