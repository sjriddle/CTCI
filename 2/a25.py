## You have two numbers represented by a linked list, where each node contains
## a single digit. The digits are stored in reverse order, such that the 1's
## digit is at the head of the list. Write a function that dds the two numbers
## and returns the sum as a linked list.

## EXAMPLE
## Input:  (7->1->6) + (5->9->2). That is, 617+295
## Output: 2->1->9. That is 912

# def add_linked_list(number1, number2):
#   return convert_list_to_int(number1) + convert_list_to_int(number2)

from helpers import Node

def convert_list_to_int(head):
  cur = head
  l = []
  while cur:
    l.append(cur.data)
    cur = cur.next

  l = l[::-1]
  return int(''.join(map(lambda x: str(x), l)))


def add_linked_list(n1, n2):
  s = 0
  i = 0
  c1, c2 = n1, n2
  while c1:
    s += ((c1.data if c1 else 0) + (c2.data if c2 else 0)) * (10**i)
    i += 1
    if c1:
      c1 = c1.next
    if c2:
      c2 = c2.next

  return s


def add_linked_list_1(n1, n2, p = 0):
  s = ((n1.data if n1 else 0) + (n2.data if n2 else 0)) * (10 ** p)
  if (n1 and n1.next) or (n2 and n2.next):
    return s + add_linked_list_1(n1.next if n1 else None, n2.next if n2 else None, p + 1)
  else:
    return s


def number_to_linked_list(n):
  head = None
  for i in str(n):
    tmp = Node(int(i))
    tmp.next = head
    head = tmp

  return head