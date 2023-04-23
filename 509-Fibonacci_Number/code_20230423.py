class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n

        results = list()
        for i in range(n+1):
            if i == 0 or i == 1:
                results.append(i)
            else:
                results.append(results[i-1] + results[i-2])
        
        return results[-1]
