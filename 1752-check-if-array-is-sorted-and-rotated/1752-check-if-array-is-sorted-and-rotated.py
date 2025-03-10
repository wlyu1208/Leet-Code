class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        rotated = 0

        for i in range(n):
            if nums[i] > nums[(i+1) % n]:
                rotated += 1
                if rotated > 1:
                    return False
        
        return True