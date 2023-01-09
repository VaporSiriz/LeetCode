# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def get_parents(node):
            parents = []
            pointer_root = root
            while True:
                parents.append(pointer_root)
                if pointer_root.val == node.val:
                    break
                if pointer_root.val > node.val:
                    pointer_root = pointer_root.left
                else:
                    pointer_root = pointer_root.right
            return parents
        p_parents = get_parents(p)
        q_parents = get_parents(q)
        result = None
        for pair in zip(p_parents, q_parents):
            p_parent, q_parent = pair
            print(f"{p_parent.val}, {q_parent.val}")
            if p_parent.val != q_parent.val:
                break
            result = p_parent
        return result