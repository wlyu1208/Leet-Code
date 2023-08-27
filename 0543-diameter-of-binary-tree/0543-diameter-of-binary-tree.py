# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.diameter = 0

    def get_diameter(self, node):
        l = self.get_diameter(node.left) if node.left else 0
        r = self.get_diameter(node.right) if node.right else 0

        self.diameter = (l + r) if (l + r) > self.diameter else self.diameter

        return 1 + (l if l > r else r)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.get_diameter(root)
        return self.diameter
        