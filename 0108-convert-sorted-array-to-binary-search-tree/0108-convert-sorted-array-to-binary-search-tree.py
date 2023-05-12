# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def buildBST(self, node: Optional[TreeNode], nums: List[int]):
        if len(nums)==0:
            return None
        middle = len(nums)//2
        #print(f"middle : {middle}, nums : {nums}")
        node = TreeNode(val=nums[middle])
        node.left = self.buildBST(node, nums[:middle])
        node.right = self.buildBST(node, nums[middle+1:])
        return node
    
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        root = self.buildBST(node=None, nums=nums)
        print(f"root : {root}")
        return root