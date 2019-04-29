import unittest, sys

from a27 import list_intersection, list_length, get_kth_node
from helpers import Node, list_to_linked_list

class Test27(unittest.TestCase):

  def test_list_lnegth(self):
    head = list_to_linked_list([0, 7, 1, 6, 2])
    result = list_length(head)
    self.assertEqual(result, 5)

  def test_get_kth_node(self):
    head = list_to_linked_list([0, 7, 1])
    result = get_kth_node(head, 0)
    self.assertEqual(result, head)

    head = list_to_linked_list([0, 7, 1])
    result = get_kth_node(head, 1)
    self.assertEqual(result, head.next)

    head = list_to_linked_list([0, 7, 1])
    result = get_kth_node(head, 2)
    self.assertEqual(result, head.next.next)

    head = list_to_linked_list([0, 7, 1])
    result = get_kth_node(head, 3)
    self.assertEqual(result, head.next.next.next)

  def test_reverse_list(self):
    head1 = list_to_linked_list([0, 7, 1, 6, 2])
    head2 = list_to_linked_list([5, 4])

    head2.next.next = head1.next.next.next

    node = list_intersection(head1, head2)
    self.assertEqual(node, head2.next.next)

if __name__ == '__main__':
    unittest.main()
