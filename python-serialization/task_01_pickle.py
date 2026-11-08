#!/usr/bin/python3
"""A module for serializing and deserializing custom Python objects using pickle."""
import pickle


class CustomObject:
    """A custom class representing a person with name, age, and student status."""

    def __init__(self, name, age, is_student):
        """Initialize the CustomObject instance.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
            is_student (bool): True if the person is a student, False otherwise.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print out the object's attributes in the specified format."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Serialize the current instance of the object and save it to a file.

        Args:
            filename (str): The filename to save the pickled object to.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Load and return an instance of CustomObject from a file.

        Args:
            filename (str): The filename to load the pickled object from.

        Returns:
            CustomObject or None: The deserialized instance, or None if an error occurs.
        """
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except (FileNotFoundError, EOFError, pickle.UnpicklingError, Exception):
            return None
