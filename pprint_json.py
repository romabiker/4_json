import json
import os
import sys


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)


def pretty_print_json(jsn_data):
    pretty_jsn = json.dumps(
                        jsn_data,
                        indent=4,
                        sort_keys=True,
                        ensure_ascii=False
                        )
    print(pretty_jsn)


if __name__ == '__main__':
    if not len(sys.argv) > 1:
        print('\nEnter: python3 pprint_json.py "filepath"\n')
    jsn_filepath = sys.argv[1]
    jsn_data = load_data(jsn_filepath)
    if not jsn_data:
        print('filepath does not exist')
    pretty_print_json(jsn_data)
