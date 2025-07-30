class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_n = max(nums)
        con_len = 0
        answer = 0
        for n in nums:
            if n == max_n:
                con_len += 1
            else:
                con_len = 0
            answer = max(answer, con_len)
        return answer