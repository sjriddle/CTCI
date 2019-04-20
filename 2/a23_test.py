import unittest, sys

from a23 import delete_node
from helpers import Node, list_to_head

class Test23(unittest.TestCase):

    def test_a1(self):

        head = list_to_head([1, 2, 3, 4, 5, 6])

        delete_node(head.next.next)
        self.assertEqual(head.toList(), [1, 2, 4, 5, 6])

if __name__ == '__main__':
    unittest.main()
