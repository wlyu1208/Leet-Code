class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff = [0] * (n + 1)

        for l, r in queries:
            diff[l] -= 1
            if r + 1 < n:
                diff[r + 1] += 1
        
        _sum = 0

        for i in range(n):
            _sum += diff[i]
        
            if nums[i] > -_sum:
                return False
        
        return True
