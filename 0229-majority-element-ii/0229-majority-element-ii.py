from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        appr = math.floor(len(nums) / 3)
        counter = Counter(nums)
        ans = set()
        for k, v in counter.items():
            if v > appr:
                ans.add(k)
        
        return list(ans)