from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __iter__(self):
        pointer = self
        while pointer is not None:
            yield pointer.val
            pointer = pointer.next

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    nodes = []
    pointer_head = head
    while pointer_head is not None:
        nodes.append(pointer_head)
        pointer_head = pointer_head.next
    
    len_list = len(nodes)
    for i in range(len_list-1, 0, -1):
        nodes[i].next = nodes[i-1]
    nodes[0].next = None
    head = nodes[len_list-1]
    return head

l = ListNode(val=1)
l.next = ListNode(val=2)
l.next.next = ListNode(val=3)
l.next.next.next = ListNode(val=4)
l.next.next.next.next = ListNode(val=5)

# for node in iter(l):
#     print(node)

nl = reverseList(l)
for node in iter(nl):
    print(node)
