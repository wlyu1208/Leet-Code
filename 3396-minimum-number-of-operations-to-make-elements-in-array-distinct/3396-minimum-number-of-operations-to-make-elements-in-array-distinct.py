class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        answer = 0
        while len(nums) > len(set(nums)):
            # new_nums = nums[3:]
            # nums = new_nums
            nums = nums[3:]
            answer += 1
        return answer