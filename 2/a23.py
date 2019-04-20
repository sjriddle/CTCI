## Implement an algorithm to delete a node in the middle (i.e any node but the
## first or last node, not necessarily the exact middle) of a singly linked list,
## given only access to that node

## EXAMPLE
## Input:  The node c from linked list a->b->c->d->e->f
## Output: Nothing is returned, but the new linked list is a->b->d->e->f


# Memory: O(1)
# CPU: O(1)
def delete_node(node):
  node.data = node.next.data
  node.next = node.next.next
