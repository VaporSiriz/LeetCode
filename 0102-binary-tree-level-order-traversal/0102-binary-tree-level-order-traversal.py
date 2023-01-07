# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = {}
        count = 0
        if root is not None:
            nodes[count] = [root]
            while len(nodes[count])!=0:
                count += 1
                nodes[count] = []
                for node in nodes[count-1]:
                    if node.left is not None:
                        nodes[count].append(node.left)
                    if node.right is not None:
                        nodes[count].append(node.right)
        result = []
        for level in nodes.keys():
            if len(nodes[level]) != 0:
                result.append([ node.val for node in nodes[level]])
        return result