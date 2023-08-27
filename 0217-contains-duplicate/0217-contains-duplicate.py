from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        cnts = Counter(nums)

        for i in cnts:
            if cnts[i] != 1:
                return True
        return False