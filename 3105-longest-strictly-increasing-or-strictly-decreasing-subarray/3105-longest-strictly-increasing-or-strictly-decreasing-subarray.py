class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc, dec = 1, 1
        n = len(nums)
        _max = 1
        for i in range(1, n):
            if nums[i-1] < nums[i]:
                inc += 1
                dec = 1
            elif nums[i-1] > nums[i]:
                dec += 1
                inc = 1
            else:
                inc, dec = 1, 1
            _max = max(inc, dec, _max)
        return _max