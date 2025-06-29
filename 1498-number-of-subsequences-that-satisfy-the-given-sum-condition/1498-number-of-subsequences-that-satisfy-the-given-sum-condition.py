class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9 + 7
        nums.sort()
        n = len(nums)

        pow2 = [1] * n
        for i in range(1, n):
            pow2[i] = (pow2[i-1] * 2) % MOD
        
        l, r = 0, n-1
        answer = 0

        while l <= r:
            if nums[l] + nums[r] <= target:
                answer = (answer + pow2[r - l]) % MOD
                l += 1
            else:
                r -= 1

        return answer