class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        left = [nums[0]] * n
        right = [nums[-1]] * n

        for i in range(1, n-1):
            left[i] = max(left[i-1], nums[i])
        for i in range(n-2, 0, -1):
            right[i] = max(nums[i], right[i+1])
        # right = right[::-1]
        # print(left)
        # print(right)
        _max = 0
        for i in range(1, n-1):
            _max = max((left[i-1] - nums[i]) * right[i+1], _max)
        return _max