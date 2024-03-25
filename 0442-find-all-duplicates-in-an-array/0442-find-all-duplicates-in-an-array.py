class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        return [k for k, v in counter.items() if v != 1]