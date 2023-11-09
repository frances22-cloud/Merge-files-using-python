"""
Tasks contains all the functions that will be reused in the codebase
"""
import json
from typing import List, Any
import pandas as pd


def read_json(file_path: str) -> List[Any]:
    """This function reads json files and returns them in a list of Any data type."""
    with open(file_path, "r") as json_file:
        data = json.load(json_file)
        return data


def merge_lists(file_path: str, json_list: str) -> List[Any]:
    """This function merges an infinite number of all the lists in range of data source"""
    merged_list = []
    for json_data in json_list:
        merged_list.append(pd.DataFrame(read_json(file_path + json_data + ".json")))
    return merged_list
