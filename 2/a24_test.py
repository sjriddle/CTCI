import unittest, sys

from a24 import partition
from helpers import Node, list_to_head

class Test24(unittest.TestCase):

    def test_a1(self):

        head = list_to_head([3, 5, 8, 5, 10, 2, 1])
        result = partition(5, head)
        self.assertEqual(result.toList(), [3, 2, 1, 5, 8, 5, 10])

        head = list_to_head([5, 6, 6])
        result = partition(5, head)
        self.assertEqual(result.toList(), [5, 6, 6])

        head = list_to_head([5, 6, 6])
        result = partition(10, head)
        self.assertEqual(result.toList(), [5, 6, 6])

if __name__ == '__main__':
    unittest.main()
