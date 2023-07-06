class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = 10**6

        l, total= 0, 0

        for r in range(len(nums)):
            total += nums[r]

            while total >= target:
                ans = min(r-l+1, ans)
                total -= nums[l]
                l += 1
        
        return 0 if ans == 10**6 else ans
