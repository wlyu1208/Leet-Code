class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = set()
        l = 0
        current_sum = 0
        max_sum = 0

        for r in range(len(nums)):
            while nums[r] in seen:
                current_sum -= nums[l]
                seen.remove(nums[l])
                l += 1
            
            current_sum += nums[r]
            seen.add(nums[r])
            max_sum = max(max_sum, current_sum)

        return max_sum