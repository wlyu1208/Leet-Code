class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()

        for i in range(len(nums)-1, -1, -1):
            if i < 2:
                break
            longest = nums[i]
            rest_sum = sum(nums[:i])
            if rest_sum > longest:
                return rest_sum + longest

        return -1