#!/usr/bin/python3
"""Defines a custom list class VerboseList that prints notifications
upon modification.
"""


class VerboseList(list):
    """A list subclass that prints notifications on append, extend,
    remove, and pop.
    """

    def append(self, item):
        """Add an item to the end of the list and print a message."""
        super().append(item)
        print(f"Added {item} to the list.")

    def extend(self, iterable):
        """Extend the list by appending elements from the iterable

        and print a message with the count of added items.
        """
        items = list(iterable)
        super().extend(items)
        print(f"Extended the list with {len(items)} items.")

    def remove(self, item):
        """Remove the first occurrence of an item and print a message."""
        print(f"Removed {item} from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Remove and return item at index (default last) and print a message."""
        item = self[index]
        print(f"Popped {item} from the list.")
        return super().pop(index)
