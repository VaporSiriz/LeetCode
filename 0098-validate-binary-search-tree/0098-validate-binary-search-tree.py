# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check_parent(parents, node_val):
            flag = True
            for parent in parents:
                parent_val, direction = parent
                print(f"{direction} - {node_val} {'<?' if direction == 'l' else '>?'} {parent_val}")
                flag = node_val < parent_val if direction == 'l' else node_val > parent_val
                if not flag:
                    break
            return flag


        queue = []
        if root.left is not None:
            if root.left.val < root.val:
                queue.append((root.left, 'l', [(root.val, 'l')]))
            else:
                return False
        if root.right is not None:
            if root.right.val > root.val:
                queue.append((root.right, 'r', [(root.val, 'r')]))
            else:
                return False

        while len(queue)!=0:
            node, direction, parents = queue.pop()
            left: TreeNode = node.left
            right: TreeNode = node.right
            print(f"{node.val}, {direction}, {parents}")
            if left is not None:
                print(f"left : {left.val} <? {node.val}")
                if left.val < node.val and check_parent(parents, left.val):
                    queue.append((left, 'l', parents+[(node.val, 'l')]))
                else:
                    return False
            if right is not None:
                print(f"right : {right.val} >? {node.val}")
                if right.val > node.val and check_parent(parents, right.val):
                    queue.append((right, 'r', parents+[(node.val, 'r')]))
                else:
                    return False
        return True