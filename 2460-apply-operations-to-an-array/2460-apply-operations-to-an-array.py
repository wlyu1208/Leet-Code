class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n-1):
            if nums[i] != nums[i+1]:
                continue
            else:
                nums[i] *= 2
                nums[i+1] = 0
        ans = []
        for _n in nums:
            if _n != 0:
                ans.append(_n)
        
        while len(ans) != n:
            ans.append(0)
        
        return ans