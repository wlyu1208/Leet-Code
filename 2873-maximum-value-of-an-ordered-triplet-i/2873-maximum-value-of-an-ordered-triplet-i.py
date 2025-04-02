class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        left_max = [nums[0]]
        right_max = [nums[-1]]
        n = len(nums)

        for i in range(1, n):
            left_max.append(max(left_max[i-1], nums[i]))

        for j in range(n-2, -1, -1):
            right_max.append(max(right_max[n-2-j], nums[j]))
        right_max = right_max[::-1]
        _max = 0
        for i in range(1, n-1):
            _max = max(_max, (left_max[i-1] - nums[i]) * right_max[i+1])
        return _max