#!/usr/bin/python3

"""Takes all passed arguements and save them to a file"""

import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    """Entry point."""
    filename = 'add_item.json'

    json_file = open(filename, 'a+')
    json_file.close()

    try:
        saved_args = load_from_json_file(filename)
        for i in sys.argv[1:]:
            saved_args.append(i)
    except json.decoder.JSONDecodeError:
        saved_args = sys.argv[1:]
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    save_to_json_file(saved_args, filename)


if __name__ == "__main__":
    main()
