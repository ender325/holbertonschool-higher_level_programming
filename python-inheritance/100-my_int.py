#!/usr/bin/python3
"""Defines a rebel integer class MyInt that inherits from int."""


class MyInt(int):
    """Represent an integer with inverted == and != operators."""

    def __eq__(self, other):
        """Invert the == operator."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Invert the != operator."""
        return super().__eq__(other)
