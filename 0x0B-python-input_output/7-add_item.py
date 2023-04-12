#!/usr/bin/python3
"""The add_item module"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    """Add all command line argument(s) to a Python list,
    and save it/them to a file
    """
    try:
        my_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        my_list = []

    my_list += sys.argv[1:]
    save_to_json_file(my_list, "add_item.json")


if __name__ == "__main__":
    main()
