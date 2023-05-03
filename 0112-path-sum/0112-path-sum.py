# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        stack = [] if not root else [(root, False, False)]
        top_index = -1 if not root else 0
        amount = 0
        while top_index > -1:
            top, lflag, rflag = stack.pop()
            
            if not lflag and not rflag:
                amount += top.val
            #print(f"{top.val} | {lflag}-{rflag}, amount : {amount}, top_index : {top_index}")
            
            # leaf
            if not top.left and not top.right:
                print(f"{amount} ?= {targetSum}")
                if amount == targetSum:
                    return True
                top_index -= 1
                amount -= top.val
                continue
            
            if lflag and rflag:
                amount -= top.val
                top_index -= 1
                continue
            
            if not lflag and top.left:
                stack.append((top, True, rflag))
                stack.append((top.left, False, False))
                top_index += 1
                continue
                
            if not rflag and top.right:
                stack.append((top, lflag, True))
                stack.append((top.right, False, False))
                top_index += 1
                continue
                
            if (not lflag and not top.left) or (not rflag and not top.right):
                amount -= top.val
                
            top_index -= 1
        return False