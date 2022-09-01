#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dict = {}
    keys_2_del = []
    if value not in a_dictionary.values():
        return a_dictionary
    else:
        for key, val in a_dictionary.items():
            if val == value:
                keys_2_del.append(key)
            else:
                new_dict[key] = val
        if keys_2_del:
            for key in keys_2_del:
                del a_dictionary[key]

    return new_dict
