# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        l = defaultdict(list)
        def dfs(node, h):
            if node is None:
                return
            l[h].append(node.val)
            dfs(node.left, h + 1)
            dfs(node.right, h + 1)
        dfs(root, 0)
        return l.values()