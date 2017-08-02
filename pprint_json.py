import json
import sys


def load_data(filepath):
    with open(filepath, 'r') as file:
        parsed = json.load(file)
    return parsed


def pretty_print_json(data):
    pretty_jsn = json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False)
    print(pretty_jsn)


if __name__ == '__main__':
    jsn_file = sys.argv[1]
    jsn_data = load_data(jsn_file)
    pretty_print_json(jsn_data)
