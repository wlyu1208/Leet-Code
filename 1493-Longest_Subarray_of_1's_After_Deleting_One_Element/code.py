class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if 0 not in nums:
            return len(nums) - 1
        prev = -1

        cnt = 0
        ans = -1

        for i in nums:
            if i:
                cnt += 1
            else:
                prev = cnt
                cnt = 0
            
            ans = max(ans, cnt)
            ans = max(ans, cnt + prev)

        return ans
