# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        pointer = root
        right_side = []
        stack = []
        if root is not None:
            right_side.append(root.val)
            if root.right != None:
                stack.append(root.right)
            if root.left != None:
                stack.append(root.left)

            while len(stack)!=0:
                # put right first
                tmp_stack = []
                print(f"stack : {stack}")
                print(f"right_side : {right_side}")
                right_side.append(stack[0].val)
                stack.reverse()
                while len(stack)!=0:
                    node = stack.pop()
                    if node.right:
                        tmp_stack.append(node.right)
                    if node.left:
                        tmp_stack.append(node.left)
                print(f"tmp_stack : {tmp_stack}")
                print(f"reverse tmp_stack : {tmp_stack}")
                stack = tmp_stack
        return right_side