# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        pointer = head
        while pointer is not None:
            nodes.append(pointer)
            pointer = pointer.next
        length = len(nodes)
        middle = int(length/2)# if length%2==0 else int(length/2)
        
        node = nodes[middle]
        
        return node