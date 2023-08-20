# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def get_depth(node):
            if not node:
                return 0
            return 1 + max(get_depth(node.left), get_depth(node.right))
        
        if not root:
            return True
        
        l = get_depth(root.left)
        r = get_depth(root.right)
        
        return abs(l - r) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)