class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()

        for i in range(1, len(nums)+1):
            cnt = 0
            for num in nums:
                if num >= i:
                    cnt += 1
            if cnt == i:
                return i
        return -1