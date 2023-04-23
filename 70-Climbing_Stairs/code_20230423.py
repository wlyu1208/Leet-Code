class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return n
        
        r_s = [1, 2]

        for i in range(2, n):
            r_s.append(r_s[i-1] + r_s[i-2])
        
        return r_s[-1]
