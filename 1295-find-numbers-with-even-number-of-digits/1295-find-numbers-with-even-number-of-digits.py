class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        cnt = 0

        for n in nums:
            if len(str(n)) % 2 == 0:
                cnt += 1
        return cnt