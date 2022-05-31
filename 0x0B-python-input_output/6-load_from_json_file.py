#!/usr/bin/python3
import json
""" Create object from a JSON file """


def load_from_json_file(filename):
    """ function that creates an Object from a “JSON file”
    """
    with open(filename, mode='r', encoding='utf-8') as f:
        return json.load(f)
