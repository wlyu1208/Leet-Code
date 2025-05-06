class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        answer = [0] * n

        for i in range(n):
            answer[i] = nums[nums[i]]
        
        return answer