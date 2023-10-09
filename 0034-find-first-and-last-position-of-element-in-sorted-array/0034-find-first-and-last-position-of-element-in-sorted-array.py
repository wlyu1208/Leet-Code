class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start, end, n = -1, -1, len(nums)

        for i in range(n):
            if nums[i] == target:
                start = i
                break

        if start == -1:
            return [-1, -1]
        
        for i in range(n - 1, -1, -1):
            if nums[i] == target:
                if nums[i] == target:
                    end = i
                    break
        
        return [start, end]