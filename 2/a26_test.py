import unittest, sys

from a26 import reverse_list, is_list_palindrome
from helpers import Node, list_to_linked_list

class Test26(unittest.TestCase):

    def test_reverse_list(self):
        result = reverse_list(list_to_linked_list([7, 1, 6, 2]))
        self.assertEqual(result.toList(), [2, 6, 1, 7])

        result = reverse_list(list_to_linked_list([1]))
        self.assertEqual(result.toList(), [1])

    def test_is_list_palindrome(self):
        result = is_list_palindrome(list_to_linked_list([1]))
        self.assertTrue(result)

        result = is_list_palindrome(list_to_linked_list([7, 1, 6, 2]))
        self.assertFalse(result)

        result = is_list_palindrome(list_to_linked_list([7, 1, 7]))
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
