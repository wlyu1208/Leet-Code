class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        track = [nums[0]]
        last_max = nums[0]
        remember_max = nums[0]
        
        for i in range(1, len(nums)):
            cur_max = max(last_max + nums[i], nums[i])
            remember_max = max(cur_max, remember_max)
            last_max = cur_max
        
        return remember_max
