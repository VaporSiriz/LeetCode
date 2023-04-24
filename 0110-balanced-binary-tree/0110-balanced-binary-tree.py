# Definition for a binary tree node.
class Solution:
    def check_height(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
       # print(f"node : {node}")
        if node.left is None and node.right is None:
            return 1
        lsub = self.check_height(node.left) if node.left else 0
        if lsub==-1:
            return -1
        rsub = self.check_height(node.right) if node.right else 0
        if rsub==-1:
            return -1
        #print(f"{node.val}: {lsub}-{rsub}")
        return max(lsub, rsub) + 1 if abs(lsub-rsub)<=1 else -1
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        height_diff = self.check_height(root)
        #print(f"height : {height}, diff : {diff}")
        return height_diff != -1