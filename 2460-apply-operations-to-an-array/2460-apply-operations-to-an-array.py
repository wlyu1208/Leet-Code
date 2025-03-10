class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n= len(nums)
        idx = 0

        for i in range(n):
            if i < n-1 and nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0

            if nums[i] != 0:
                nums[idx] = nums[i]
                if idx != i:
                    nums[i] = 0
                idx += 1
        
        return nums