class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        cnt_even, cnt_odd = 0, 0

        for n in nums:
            if n % 2 == 1:
                cnt_odd += 1
            else:
                cnt_even += 1
        
        even_dp, odd_dp = 0, 0
        for n in nums:
            if n % 2 == 0:
                even_dp = max(even_dp, odd_dp + 1)
            else:
                odd_dp = max(odd_dp, even_dp + 1)
        
        return max(cnt_even, cnt_odd, even_dp, odd_dp)
