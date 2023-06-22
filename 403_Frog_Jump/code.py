class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)

        dp = {stone: set() for stone in stones}
        dp[0].add(0)

        for i in range(n):
            for k in set(dp[stones[i]]):
                for jump in range(k - 1, k + 2):
                    if jump and stones[i] + jump in stones:
                        dp[stones[i] + jump].add(jump)

        if dp[stones[-1]]:
            return True
        else:
            return False
