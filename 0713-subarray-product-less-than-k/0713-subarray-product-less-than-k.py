class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        count = 0
        product = 1
        l = 0

        for i, num in enumerate(nums):
            product *= num

            while product >= k:
                product /= nums[l]
                l += 1

            count += i - l + 1
        
        return count