## Implement an algorithm to find the kth to last element of singly linked list

# Memory: O(1)
# CPU: O(n)
def k_last_element(head, k):
    if k < 0:
        return None
    cur = head
    cur_2 = None
    i = 0
    while cur:
        if cur.next == None:
            return cur_2
        cur = cur.next

        if i == k:
            cur_2 = head
        if i >= k:
            cur_2 = cur_2.next
        i += 1

    return None
