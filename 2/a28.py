## Given a circular linked list, implement an algorithm that returns the node at
## the beginning of the loop in the linked list

## DEFINITION
## Circular linked list: A (corrupt) linked list in which a node's next pointer
## points to an earlier node, so as to make a loop in the linked list

## EXAMPLE
## Input:  A -> B -> C -> D -> E -> C [The same C as earlier]
## Output: C

def list_loop(head):
  s = set()
  cur = head
  while cur:
    if cur in s:
      return cur
    s.add(cur)
    cur = cur.next

  return None