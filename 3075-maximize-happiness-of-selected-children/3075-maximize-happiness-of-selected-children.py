class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        i = 0
        ans = 0
        happiness.sort(reverse=True)
        while k > 0:
            happiness[i] = max(happiness[i]-i, 0)
            ans += happiness[i]
            i += 1
            k -= 1
        return ans