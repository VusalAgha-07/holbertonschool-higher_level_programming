#!/usr/bin/python3
"""
Adds all arguments to a Python list and saves them to a file.
"""
import sys
import os

# Import functions from previous tasks
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Check if the file exists; if so, load current list. If not, start with empty.
if os.path.exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

# Add command-line arguments (starting from index 1) to the list
# sys.argv[1:] takes all arguments after the script name
items.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json_file(items, filename)
