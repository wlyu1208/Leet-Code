class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []

        def backtrack(index):
            if index == n:
                result.append(nums[:])
                return

            for i in range(index, n):
                nums[index], nums[i] = nums[i], nums[index]
                backtrack(index + 1)
                nums[index], nums[i] = nums[i], nums[index]
        
        backtrack(0)
        return result
