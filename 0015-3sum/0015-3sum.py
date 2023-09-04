from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []
        n = len(nums)

        for i in range(n - 2):
            if nums[i] > 0:
                break
            l = i + 1
            r = n - 1
            while l < r:
                _sum = nums[i] + nums[l] + nums[r]
                if _sum < 0:
                    l += 1
                elif _sum > 0:
                    r -= 1
                else:
                    threes = [nums[i], nums[l], nums[r]]
                    if threes not in answer:
                        answer.append(threes)
                    while l < r and nums[l] == threes[1]:
                        l += 1
                    while l < r and nums[r] == threes[2]:
                        r -= 1

        return answer
