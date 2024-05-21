class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = [[]]

        for num in nums:
            answer += [current + [num] for current in answer]
        return answer