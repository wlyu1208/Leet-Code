class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        q = [1, 2]
        
        for i in range(2, n):
            q.append(q[i-1] + q[i-2])
        
        return q[-1]
