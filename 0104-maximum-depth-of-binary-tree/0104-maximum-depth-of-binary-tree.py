# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        cursor = root
        nodes = []
        depth = 0
        if root is not None:
            nodes.append(root)
            depth += 1
        while len(nodes)!=0:
            tmp_nodes = []
            for node in nodes:
                if node.left is not None:
                    tmp_nodes.append(node.left)
                if node.right is not None:
                    tmp_nodes.append(node.right)
            if len(tmp_nodes)!=0:
                depth += 1
            nodes = tmp_nodes
        return depth
                