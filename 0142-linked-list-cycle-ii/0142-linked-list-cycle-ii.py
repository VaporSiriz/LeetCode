# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node_set = {}
        pointer_head = head
        pos = 0
        while pointer_head is not None:
            if pointer_head in node_set:
                return pointer_head
            node_set[pointer_head] = pos
            pos += 1
            pointer_head = pointer_head.next
        return None