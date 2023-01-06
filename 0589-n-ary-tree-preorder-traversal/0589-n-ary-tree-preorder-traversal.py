"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        path = []
        #print(root.val)
        if root is not None:
            path.append(root.val)
            for child in root.children:
                if child is not None:
                    path += self.preorder(child)
            return path
        