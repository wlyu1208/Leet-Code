# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, max_h, cur_h):
        if node is None:
            return 0
        if cur_h == max_h:
            return node.val
        
        left = self.dfs(node.left, max_h, cur_h + 1)
        right = self.dfs(node.right, max_h, cur_h + 1)
        
        return left + right
    
    
    def get_height(self, node):
        if node is None:
            return 0
        
        l = self.get_height(node.left)
        r = self.get_height(node.right)
        
        return 1 + max(l, r)
    
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        max_h = self.get_height(root)
        
        s = self.dfs(root, max_h, 1)
        
        return s