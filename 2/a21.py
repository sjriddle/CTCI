## Write code to remove dupicates from an unsorted list

# Memory: O(n)
# CPU: O(n)
def remove_dupes_a(head):
    x = set()
    cur = head
    prev = None
    while cur:
        if cur.data not in x:
            x.add(cur.data)
            prev = cur
        else:
            prev.next = cur.next

        cur = cur.next
    return head


# Memory: O(1)
# CPU: O(n^2)
def remove_dupes_b(head):
    cur = head
    prev = None
    while cur:
        prev = cur
        cc = cur.next
        while cc:
            if cc.data == cur.data:
                prev.next = cc.next
            else:
                prev = cc
            cc = cc.next
        cur = cur.next

    return head
