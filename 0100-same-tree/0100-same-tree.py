# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self, fnode: Optional[TreeNode], snode: Optional[TreeNode]) -> bool:
        if (fnode is None) ^ (snode is None):
            return False
        if fnode is None and snode is None:
            return True
        
        if fnode.val != snode.val:
            return False
        
        else:
            if not self.preorder(fnode.left, snode.left):
                return False
            if not self.preorder(fnode.right, snode.right):
                return False
        
        return True
        
        
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.preorder(p, q)