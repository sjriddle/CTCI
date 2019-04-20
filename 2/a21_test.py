import unittest

from a21 import remove_dupes_a, remove_dupes_b
from helpers import Node

class Test21(unittest.TestCase):

    def test_a1(self):
        head = Node(1)
        head.next = Node(1)
        head.next.next = Node(2)
        head.next.next.next = Node(2)
        head.next.next.next.next = Node(2)
        head.next.next.next.next.next = Node(3)

        result = remove_dupes_a(head)
        self.assertEqual(result.toList(), [1, 2, 3])

    def test_a2(self):
        head = Node(1)

        result = remove_dupes_a(head)
        self.assertEqual(result.toList(), [1])

    def test_a3(self):
        head = Node(1)
        head.next = Node(1)

        result = remove_dupes_a(head)
        self.assertEqual(result.toList(), [1])

    def test_b1(self):
        head = Node(1)
        head.next = Node(1)
        head.next.next = Node(2)
        head.next.next.next = Node(2)
        head.next.next.next.next = Node(2)
        head.next.next.next.next.next = Node(3)

        result = remove_dupes_b(head)
        self.assertEqual(result.toList(), [1, 2, 3])

    def test_b2(self):
        head = Node(1)

        result = remove_dupes_b(head)
        self.assertEqual(result.toList(), [1])

    def test_b3(self):
        head = Node(1)
        head.next = Node(1)

        result = remove_dupes_b(head)
        self.assertEqual(result.toList(), [1])


if __name__ == '__main__':
    unittest.main()