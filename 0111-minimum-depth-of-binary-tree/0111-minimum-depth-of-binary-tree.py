# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        min_depth = 100000 if root else 0
        nodes = [(root, 1)] if root else []
        while len(nodes)!=0:
            node, depth = nodes.pop()
            #print(f"node : {node}")
            if not node.left and not node.right:
                #print(f"depth : {depth}, min_depth : {min_depth}")
                min_depth = depth if depth < min_depth else min_depth
                continue
                
            if node.left:
                nodes.append((node.left, depth+1))
            if node.right:
                nodes.append((node.right, depth+1))
                
        return min_depth