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


def detectCycle(head: Optional[ListNode]) -> Optional[ListNode]:
    node_set = {}
    pointer_head = head
    pos = 0
    while pointer_head is not None:
        if pointer_head.val in node_set:
            return node_set[pointer_head.val]
        node_set[pointer_head.val] = pos
        pos += 1
        pointer_head = pointer_head.next
    return -1

l = ListNode(val=1)
#l.next = ListNode(val=2)
#l.next.next = ListNode(val=3)
#l.next.next.next = ListNode(val=4)
# l.next.next.next.next = ListNode(val=5)

nl = detectCycle(l)
print(f"return {nl}")