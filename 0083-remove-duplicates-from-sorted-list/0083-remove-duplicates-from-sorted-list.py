# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        while node is not None:
            next_node = node.next
            while next_node is not None:
                if node.val != next_node.val:
                    break
                next_node = next_node.next
            node.next = next_node
            node = node.next
        return head