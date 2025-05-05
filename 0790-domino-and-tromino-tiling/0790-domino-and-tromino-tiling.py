class Solution:
    def numTilings(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        MOD = 10 ** 9 + 7

        dp = [0] * (n+1)

        dp[0], dp[1], dp[2] = 1, 1, 2

        for i in range(3, n+1):
            dp[i] = (2 * dp[i-1] + dp[i-3]) % MOD
    
        return dp[n]