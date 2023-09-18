from collections import deque
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        q1 = deque([1])
        q2 = deque([1])
        n = len(nums)

        for i in range(n - 1):
            last = q1[-1]
            q1.append(q1[-1] * nums[i])
        for i in range(n-1, 0, -1):
            q2.appendleft(q2[0] * nums[i])
        answer = []
        for i in range(n):
            answer.append(q1[i] * q2[i])
        
        return answer

