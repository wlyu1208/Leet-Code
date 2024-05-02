class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return -1

        nums.sort()
        i, n = 0, len(nums)
        while i < n-1 and nums[i] < 0:
            key = nums[i] * -1
            if key in nums:
                return key
            i += 1
        return -1