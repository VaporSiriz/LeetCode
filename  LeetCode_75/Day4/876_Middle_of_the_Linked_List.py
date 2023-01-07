from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __iter__(self):
        pointer = self
        while pointer is not None:
            yield pointer.val
            pointer = pointer.next


def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
    nodes = []
    pointer = head
    while pointer is not None:
        nodes.append(pointer)
        pointer = pointer.next
    length = len(nodes)
    middle = int(length/2)# if length%2==0 else int(length/2)
    
    node = nodes[middle]
    
    return node

l = ListNode(val=1)
l.next = ListNode(val=2)
l.next.next = ListNode(val=3)
l.next.next.next = ListNode(val=4)
l.next.next.next.next = ListNode(val=5)

nl = middleNode(l)
for node in iter(nl):
    print(node)