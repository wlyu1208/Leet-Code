class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        
        while left < right:
            if nums[left] == target:
                return left
            
            pivot = (left + right) // 2
            
            if nums[pivot] > target:
                right -= 1
            else:
                left += 1
        
        return -1
