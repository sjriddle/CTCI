## Implement a function to check if a linked list is a palindrome
from helpers import Node

def is_list_palindrome(head):
  rev = reverse_list(head)
  cur1 = head
  cur2 = rev
  while cur1:
    if cur1.data != cur2.data:
      return False
    cur1 = cur1.next
    cur2 = cur2.next

  return True



def reverse_list(head):
  new_head = None
  cur = head
  while cur:
    node = Node(cur.data)
    node.next = new_head
    new_head = node
    cur = cur.next

  return new_head