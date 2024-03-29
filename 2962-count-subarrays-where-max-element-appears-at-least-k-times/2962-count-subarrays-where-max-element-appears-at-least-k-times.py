class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        _max = max(nums)
        l = 0
        cnt = 0
        ans = 0

        for r in range(len(nums)):
            if nums[r] == _max:
                cnt += 1
            
            while cnt >= k:
                if nums[l] == _max: 
                    cnt -= 1
                l += 1
            ans += l

        return ans    
        