class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        l, r = nums[-k:], nums[:-k]
        new_array = l + r
        for i in range(len(nums)):
            nums[i] = new_array[i]