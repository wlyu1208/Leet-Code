# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_v, q_v = p.val, q.val
        original = root

        while root is not None:
            if p_v < root.val and q_v < root.val:
                root = root.left
            elif p_v > root.val and q_v > root.val:
                root = root.right
            else:
                return root