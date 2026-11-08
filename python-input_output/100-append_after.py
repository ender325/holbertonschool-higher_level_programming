#!/usr/bin/python3
"""Defines a file-appending function."""


def append_after(filename="", search_string="", new_string=""):
    """Append a new line after each line containing

    a specific string in a text file.
    """
    new_lines = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            new_lines.append(line)
            if search_string in line:
                new_lines.append(new_string)

    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(new_lines)
