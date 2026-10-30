#!/usr/bin/python3
"""Unittests for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer(list=[])"""

    def test_regular_list(self):
        """Test with a standard ordered list of integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with an unordered list of integers."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test when the maximum value is at the beginning of the list."""
        self.assertEqual(max_integer([4, 1, 2, 3]), 4)

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertEqual(max_integer([]), None)

    def test_one_element_list(self):
        """Test with a list containing only one element."""
        self.assertEqual(max_integer([7]), 7)

    def test_negative_numbers(self):
        """Test with a list containing negative integers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_positive_and_negative(self):
        """Test with a list containing both positive and negative integers."""
        self.assertEqual(max_integer([-5, 2, 9, -10, 0]), 9)

    def test_floats(self):
        """Test with a list of floating-point numbers."""
        self.assertEqual(max_integer([1.5, 2.3, 0.9, 2.1]), 2.3)

    def test_mixed_ints_and_floats(self):
        """Test with a list combining integers and floats."""
        self.assertEqual(max_integer([1, 2.5, 3, 2.1]), 3)

    def test_string(self):
        """Test with a single string argument (iterated as a list of characters)."""
        self.assertEqual(max_integer("Holberton"), "t")

    def test_list_of_strings(self):
        """Test with a list of strings."""
        self.assertEqual(max_integer(["abc", "def", "xyz"]), "xyz")

    def test_empty_string_in_list(self):
        """Test with a list containing strings and an empty string."""
        self.assertEqual(max_integer(["hello", "", "world"]), "world")


if __name__ == '__main__':
    unittest.main()
