class Solution:
    def __init__(self):
        self.vals = list()
        self.min_val = 10**6

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.traverse(root)
        self.vals.sort()

        for l, r in zip(self.vals, self.vals[1:]):
            self.min_val = min(self.min_val, abs(l - r))

        return self.min_val

    def traverse(self, node):
        if node is None:
            return
        
        if node.val not in self.vals:
            self.vals.append(node.val)
        
        self.traverse(node.left)
        self.traverse(node.right)
