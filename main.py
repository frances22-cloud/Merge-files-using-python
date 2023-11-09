"""
This is the main module for this project. All function calls will be done here.
"""
import logging

import pandas as pd

import datetime

from tasks import merge_lists

FILE_PATH = "data_source/"
json_files_list = [
    "group_a_students",
    "group_b_students",
]
output_dir = "output_directory/"

if __name__ == '__main__':
    merged_data_frame = (pd.concat(
        (merge_lists(FILE_PATH, json_files_list)), axis=0, ignore_index=True
    )).to_json(output_dir + "merged_json_file.json")

    logging.basicConfig(filename=f'{output_dir}code_labs_logging.log', level=logging.INFO)
    logging.info(f'This operation was completed at {datetime.datetime.now()}')
