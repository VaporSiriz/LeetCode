# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        numbers = []
        nodes = []
        nodes = [root] if root else []
        while len(nodes)!=0:
            #print(f"{nodes} - {numbers}")
            node = nodes.pop()
            if type(node) == int:
                numbers.append(node)
            else:
                if node.right:
                    nodes.append(node.right)
                nodes.append(node.val)
                if node.left:
                    nodes.append(node.left)
        return numbers