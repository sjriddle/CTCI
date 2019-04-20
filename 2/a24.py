## Write code to partition a linked list around a value x, such that all nodes
## less than x come before all nodes greater than or equal to x. If x is
## contained within the list, the values of x only need to be after the elements
## less than x. The partition element x can appear anywhere in the "right
## partition"; it doesn't need to appear between the left and right partitions.

## EXAMPLE
## Input:  3->5->8->5->10->2->1 [partition=5]
## Output: 3->1->2->10->5->5->8

from helpers import Node

def partition(x, head):
  cur = head
  l_tail = None
  l_head = None
  h_tail = None
  h_head = None
  while cur:
    if cur.data < x:
      if not l_head:
        l_head = cur
        l_tail = cur
      else:
        l_tail.next = cur
        l_tail = l_tail.next
    else:
      if not h_head:
        h_head = cur
        h_tail = cur
      else:
        h_tail.next = cur
        h_tail = h_tail.next
    cur = cur.next

  if h_tail:
    h_tail.next = None
  if l_tail:
    l_tail.next = h_head
  else:
    l_head = h_head

  return l_head
