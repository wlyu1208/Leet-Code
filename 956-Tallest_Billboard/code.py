class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = {0:0}

        for rod in rods:
            for diff, tall in list(dp.items()):
                new_diff = diff + rod
                new_tall = tall + rod

                dp[new_diff] = max(dp.get(new_diff, 0), new_tall)

                small_rod = tall - diff + rod
                new_diff = abs(tall - small_rod)

                new_tall = max(small_rod, tall)

                dp[new_diff] = max(dp.get(new_diff, 0), new_tall)
        return dp[0]
