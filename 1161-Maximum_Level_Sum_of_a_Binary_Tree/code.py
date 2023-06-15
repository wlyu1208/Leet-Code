class Solution:
    def __init__(self):
        self.vals = dict()

    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        self.traverse(root, 1)
        
        return max(self.vals, key=self.vals.get)

    def traverse(self, node, lvl):
        if node is None:
            return
        
        if lvl in self.vals:
            self.vals[lvl] += node.val
        else:
            self.vals[lvl] = node.val

        self.traverse(node.left, lvl+1)
        self.traverse(node.right, lvl+1)
