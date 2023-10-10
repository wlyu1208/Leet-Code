from collections import Counter
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        _set = set()
        unique = []

        for n in nums:
            if n not in _set:
                _set.add(n)
                unique.append(n)

        unique.sort()
        n = len(unique)
        end = 0
        minop = float('inf')

        for start in range(n):
            while end < n and unique[end] - unique[start]< len(nums):
                end += 1
            
            minop = min(minop, len(nums) - (end - start))
        
        return minop