class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        distinct = set(nums)
        distinct_cnt = len(distinct)

        count = 0
        n = len(nums)

        for i in range(n):
            current = set()
            for j in range(i, n):
                current.add(nums[j])
                if len(current) == distinct_cnt:
                    count += (n - j)
                    break
        return count