class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        dp = [{} for _ in range(n)]

        for i in range(n):
            dp[i][0] = 1
            for j in range(i):
                diff = nums[i] - nums[j]

                if diff not in dp[j]:
                    dp[i][diff] = 2
                else: 
                    dp[i][diff] = dp[j][diff] + 1
            ans = max(ans, max(dp[i].values()))
        
        return ans
