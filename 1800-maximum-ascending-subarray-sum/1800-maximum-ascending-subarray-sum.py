class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        _max = nums[0]
        _sum = nums[0]
        n = len(nums)

        for i in range(1, n):
            if nums[i-1] < nums[i]:
                _sum += nums[i]
                _max = max(_max, _sum)
            else:
                _sum = nums[i]
                _max = max(_max, _sum)

        return _max