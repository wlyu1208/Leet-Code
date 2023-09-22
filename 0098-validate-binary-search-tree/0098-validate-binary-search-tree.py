# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(root, r, l):
            if not root:
                return True
            
            if root.val >= r or root.val <= l:
                return False
            else:
                return check(root.left, root.val, l) and check(root.right, r, root.val)
            
        return check(root, float('inf'), float('-inf'))