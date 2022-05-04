#!/usr/bin/python3
def best_score(a_dictionary):
    if isinstance(a_dictionary, dict) or len(a_dictionary) is False:
        return None

    max_value = max([a_dictionary[item] for item in a_dictionary])
    for item in a_dictionary:
        if a_dictionary[item] == max_value:
            return item
