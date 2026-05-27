#!/usr/bin/env python3
"""
Module for converting CSV data to JSON format.
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Reads data from a CSV file and converts it to a JSON file.

    Args:
        csv_filename (str): The name of the source CSV file.

    Returns:
        bool: True if conversion was successful, False otherwise.
    """
    try:
        data_list = []

        # Open the CSV file for reading
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            # Use DictReader to automatically map headers to values
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                data_list.append(row)

        # Write the list of dictionaries to data.json
        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data_list, json_file, indent=4)

        return True

    except (FileNotFoundError, IOError, PermissionError):
        return False
