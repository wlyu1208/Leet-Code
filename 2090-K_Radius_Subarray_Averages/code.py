class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        denom = 2 * k + 1

        prefix = [0]

        for x in nums:
            prefix.append(prefix[-1] + x)
        
        ans = [-1] * n

        for i in range(n):
            l, r = i - k, i + k
            if l >= 0 and r < n:
                ans[i] = int((prefix[r+1] - prefix[l]) / denom)
        
        return ans
