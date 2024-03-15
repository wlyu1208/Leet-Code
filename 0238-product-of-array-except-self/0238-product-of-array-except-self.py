class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        forward = [1] * n
        backward = [1] * n

        for i in range(1, n):
            forward[i] = forward[i-1] * nums[i-1]
        
        for i in range(n-2, -1, -1):
            backward[i] = backward[i+1] * nums[i+1]

        return [forward[i] * backward[i] for i in range(n)]