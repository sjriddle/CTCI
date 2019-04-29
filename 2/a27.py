## Given two (singly) linked lists, determine if the two lists interserct. Return
## the intersecting node. Note that the intersection is defined based on reference,
## not value. That is, if the kth node of the first linked list is the exact same
## node (by reference) as the jth node of the second linked list, then they are
## intersecting.

from helpers import Node

def list_length(head):
  cur = head
  total = 0
  while cur:
    cur = cur.next
    total += 1

  return total


def get_kth_node(head, k):
  node = head
  for i in range(k):
    node = node.next

  return node

def list_intersection(h1, h2):
  p1 = list_length(h1)
  p2 = list_length(h2)
  if p1 > p2:
    p1, p2 = p2, p1
    h1, h2 = h2, h1
  offset = p2 - p1
  new_head_2 = get_kth_node(h2, offset)

  cur = h1
  cur2 = new_head_2
  while cur:
    if cur == cur2:
      return cur
    cur2 = cur2.next
    cur = cur.next

  return None
