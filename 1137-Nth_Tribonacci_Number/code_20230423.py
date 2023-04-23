class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        elif n == 2:
            return 1
        
        results = [0, 1, 1]

        for i in range(3, n+1):
            results.append(results[i-1] + results[i-2] + results[i-3])
        
        return results[-1]
