#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Class to test max_integer function"""

    def test_ordered_list(self):
        """Test with an ordered list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with an unordered list of integers"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertEqual(max_integer([]), None)

    def test_one_element_list(self):
        """Test with a list of only one element"""
        self.assertEqual(max_integer([7]), 7)

    def test_max_at_beginning(self):
        """Test with a list where the max is at the beginning"""
        self.assertEqual(max_integer([10, 5, 8, 3]), 10)

    def test_negative_numbers(self):
        """Test with a list of negative numbers"""
        self.assertEqual(max_integer([-1, -5, -10, -2]), -1)

    def test_floats_and_integers(self):
        """Test with a list of floats and integers"""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_string_in_list(self):
        """Test with a list that contains a string (should raise TypeError)"""
        with self.assertRaises(TypeError):
            max_integer([1, "string", 3])

    def test_none_argument(self):
        """Test with None as argument (should raise TypeError)"""
        with self.assertRaises(TypeError):
            max_integer(None)

if __name__ == '__main__':
    unittest.main()
