class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def toList(self):
        res_list = [self.data]
        cur = self.next
        while cur:
            res_list.append(cur.data)
            cur = cur.next

        return res_list

def list_to_head(l):
    head = Node(l[0])
    prev = head
    for i in range(1, len(l)):
        prev.next = Node(l[i])
        prev = prev.next

    return head