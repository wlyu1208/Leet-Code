class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        answer = [1]
        for i in range(n-1):
            answer.append(answer[-1] * nums[i])
        
        r = nums[-1]
        for i in range(n-2, -1, -1):
            answer[i] *= r
            r *= nums[i]
        
        return answer