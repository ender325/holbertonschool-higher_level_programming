#!/usr/bin/python3
"""Defines a custom iterator class CountedIterator that tracks
the number of items iterated over.
"""


class CountedIterator:
    """An iterator wrapper that counts how many items have been fetched."""

    def __init__(self, iterable):
        """Initialize the iterator and counter.

        Args:
            iterable: Any iterable object (e.g., list, tuple, set).
        """
        self.iterator = iter(iterable)
        self.count = 0

    def get_count(self):
        """Return the number of items fetched so far."""
        return self.count

    def __next__(self):
        """Fetch the next item, increment the counter, and return it."""
        item = next(self.iterator)
        self.count += 1
        return item

    def __iter__(self):
        """Return the iterator object itself."""
        return self
