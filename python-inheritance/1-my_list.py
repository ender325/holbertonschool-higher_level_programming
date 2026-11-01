#!/usr/bin/python3
"""Defines a MyList class."""


class MyList(list):
    """A custom list class that inherits from list."""

    def print_sorted(self):
        """Prints the list in ascending order without modifying the original list."""
        print(sorted(self))
