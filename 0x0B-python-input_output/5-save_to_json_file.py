#!/usr/bin/python3
import json
""" Save Object to a file """


def save_to_json_file(my_obj, filename):
    """ function that writes an Object to a text file,
        using a JSON representation.
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(my_obj, f)
        """f.write(json.dumps(my_obj) + '\n')"""
