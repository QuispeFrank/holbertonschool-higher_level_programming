#!/usr/bin/python3
""" function that creates an Object from a “JSON file """
import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    size = len(sys.argv)
    lista = []
    for i in range(1, size):
        lista.append(sys.argv[i])
    new_lista = load_from_json_file('add_item.json')
    new_lista += lista
    save_to_json_file(new_lista, 'add_item.json')

except FileNotFoundError:
    save_to_json_file([], 'add_item.json')
