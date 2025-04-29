class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n, l = len(nums), 0
        _sum = 0
        count = 0
        for r, num in enumerate(nums):
            _sum += num
            score = _sum * (r-l+1)
            while score >= k:
                _sum -= nums[l]
                l += 1
                score = _sum * (r-l + 1)
            count += (r-l+1)
        return count
