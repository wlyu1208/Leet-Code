class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        
        step = 0
        factor = 2

        while n > 1:
            while n % factor == 0:
                step += factor
                n = n // factor
            factor += 1
        
        return step