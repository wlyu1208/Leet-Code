# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.dp = []
    
    def get(self, n):
        if n % 2 == 0:
            return []
        
        if self.dp[n]:
            return self.dp[n]
        
        if n == 1:
            node = TreeNode(0)
            return [node]
        
        answer = []
        for i in range(1, n, 2):
            l_idx, r_idx = i, n - i - 1
            l, r = self.get(l_idx), self.get(r_idx)

            for left in l:
                for right in r:
                    root = TreeNode(0)
                    root.left = left
                    root.right = right
                    answer.append(root)

        self.dp[n] = answer
        return answer

    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        self.dp = [[] for _ in range(n+1)]
        return self.get(n)
