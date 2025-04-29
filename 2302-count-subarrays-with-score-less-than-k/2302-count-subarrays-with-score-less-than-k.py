class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        cnt = 0
        current_length = 0
        current_sum = 0
        l = 0

        for r, x in enumerate(nums):
            current_sum += x
            current_length += 1

            while current_sum * current_length >= k:
                current_sum -= nums[l]
                current_length -= 1
                l += 1
            cnt += current_length

        return cnt