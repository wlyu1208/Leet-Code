class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = dict()

        for i in arr:
            target = i - difference

            if target in dp:
                dp[i] = 1 + dp[target]
            else:
                dp[i] = 1

        return max(list(dp.values()))
