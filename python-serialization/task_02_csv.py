#!/usr/bin/python3
"""A module to convert CSV data into JSON format."""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert data from a CSV file into a JSON file named data.json.

    Args:
        csv_filename (str): The filename of the input CSV file.

    Returns:
        bool: True if the conversion was successful, False otherwise.
    """
    try:
        # Open and read the CSV file using DictReader
        with open(csv_filename, mode="r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

        # Serialize and write the data to data.json
        with open("data.json", mode="w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

        return True
    except Exception:
        return False
