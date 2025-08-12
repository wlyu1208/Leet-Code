class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        base = 1
        MOD = 10**9 + 7
        powers = []
        while True:
            num = base ** x
            if num > n:
                break
            powers.append(num)
            base += 1
        dp = [0] * (n + 1)
        dp[0] = 1
        for p in powers:
            # print(p, dp)
            for i in range(n, p-1, -1):
                dp[i] = (dp[i] + dp[i-p]) % MOD
        return dp[n]