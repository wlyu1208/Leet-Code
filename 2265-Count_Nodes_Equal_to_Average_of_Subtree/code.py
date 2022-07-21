# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.answer = 0
        
        def iterate(node):
            if node is None:
                return (0, 0)
            
            left = iterate(node.left)
            right = iterate(node.right)
            
            total = left[0] + right [0] + node.val
            count = left[1] + right[1] + 1
            
            if total // count == node.val:
                self.answer += 1
            
            return (total, count)
            
            
        iterate(root)
        
        return self.answer
