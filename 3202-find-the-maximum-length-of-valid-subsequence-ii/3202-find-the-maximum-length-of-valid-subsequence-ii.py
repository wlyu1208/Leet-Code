class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = [[0] * k for _ in range(k)]

        res = 0
        for num in nums:
            num %= k 
            for prev in range(k):
                dp[num][prev] = dp[prev][num] + 1
            res = max(res, max(dp[num]))

        return res