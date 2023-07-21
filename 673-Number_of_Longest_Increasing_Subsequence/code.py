class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)

        dp = [1] * n
        frequency = [1] * n

        max_length = 1
        answer = 0

        for i in range(1, n):
            for j in range(i):
                if nums[i] >nums[j]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        frequency[i] = frequency[j]
                    elif dp[j] + 1 == dp[i]:
                        frequency[i] += frequency[j]
            
            max_length = max(max_length, dp[i])
        
        for i in range(n):
            if dp[i] == max_length:
                answer += frequency[i]
        return answer
