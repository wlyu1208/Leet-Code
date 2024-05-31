class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)

        ans = []

        for key, val in counter.items():
            if val >= 2:
                continue
            ans.append(key)
        
        return ans