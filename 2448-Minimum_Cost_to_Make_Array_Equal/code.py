class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        _min = 10**31

        l, r = 0, max(nums) + 1

        def calc(val):
            total = 0

            for i, x in enumerate(nums):
                total += abs(val - x) * cost[i]
            
            return total

        while l + 2 < r:
            mid_l = l + (r - l) // 3
            mid_r = l + (r - l) * 2 // 3

            if calc(mid_l) < calc(mid_r):
                r = mid_r
            else:
                l = mid_l
        
        for i in range(l, r+1):
            _min = min(_min, calc(i))
        
        return _min
