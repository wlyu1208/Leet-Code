class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        
        l, r = 0, len(nums)

        while l < r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid