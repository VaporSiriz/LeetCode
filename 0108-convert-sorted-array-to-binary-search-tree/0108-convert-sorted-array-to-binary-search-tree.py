# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def buildBST(self, node: Optional[TreeNode], nums: List[int], direction: str):
        if len(nums)==0:
            return None
        #print(f"node : {node} - nums : {nums}, {direction}")
        if len(nums)==1:
            return TreeNode(val=nums[0])
        start = 0
        end = len(nums)
        middle = (end-start)//2
        node = TreeNode(val=nums[middle])
        #print(f"{start}-{middle}-{end}")
        #print(f"l : {start}:{end if end==middle else middle}, {nums[start:middle+1 if end==middle else middle]}")
        node.left = self.buildBST(node, nums[start:middle+1 if end==middle else middle], 'l')
        
        #print(f"r : {middle+1}:{end}, {nums[middle+1:end]}")
        node.right = self.buildBST(node, nums[middle+1:end], 'r')
        return node
    
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        root = self.buildBST(node=None, nums=nums, direction='')
        print(f"root : {root}")
        return root