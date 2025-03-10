class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        idx = 0

        for i in range(n-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        
        for i in range(n):
            if nums[i] != 0:
                nums[idx] = nums[i]
                idx += 1
        
        for i in range(idx, n):
            nums[i] = 0
        
        return nums