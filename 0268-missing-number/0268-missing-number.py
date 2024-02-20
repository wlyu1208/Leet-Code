class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # nums.sort()
        # for i in range(len(nums)):
        #     if i != nums[i]:
        #         return i
        # return len(nums)

        n = len(nums)
        return n * (n+1) // 2 - sum(nums)