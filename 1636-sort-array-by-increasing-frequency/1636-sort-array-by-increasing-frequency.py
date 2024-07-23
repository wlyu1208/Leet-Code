class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)

        sort_counter = dict(sorted(counter.items(), key=lambda item: (item[1], -item[0])))

        ans = []

        for k, v in sort_counter.items():
            ans.extend([k] * v)
        return ans