class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)
        
        while start < end:
            pivot = (start + end) // 2
            
            if nums[pivot] == target:
                return pivot
            
            if target < nums[pivot]:
                end -= 1
            
            if target > nums[pivot]:
                start += 1
        return end
