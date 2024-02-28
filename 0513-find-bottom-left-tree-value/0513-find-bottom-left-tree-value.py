# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.lowest_height = -1
        self.answer = -1

    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if root.left is None and root.right is None:
            return root.val

        self.dfs(root, self.lowest_height)
        return self.answer
    
    def dfs(self, root, depth):
        if root is None:
            return
        
        if depth > self.lowest_height:
            self.lowest_height = depth
            self.answer = root.val
        
        self.dfs(root.left, depth+1)
        self.dfs(root.right, depth+1)

