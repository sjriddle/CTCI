import unittest, sys

from a22 import k_last_element
from helpers import Node, list_to_head

class Test22(unittest.TestCase):

    def test_a1(self):

        head = list_to_head([1, 2, 3, 4, 5, 6])

        result = k_last_element(head, 0)
        self.assertEqual(result.data, 6)

        result = k_last_element(head, -2)
        self.assertEqual(result, None)

        result = k_last_element(head, 6)
        self.assertEqual(result, None)

        result = k_last_element(head, 1)
        self.assertEqual(result.data, 5)

        result = k_last_element(head, 2)
        self.assertEqual(result.data, 4)

        result = k_last_element(head, 5)
        self.assertEqual(result.data, 1)

if __name__ == '__main__':
    unittest.main()