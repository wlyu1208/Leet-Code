class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        answer = []
        visit = set()
        for i, n in enumerate(nums):
            if n == key:
                for j in range(i - k, i + k + 1):
                    if j not in visit and j >= 0 and j < len(nums):
                        answer.append(j)
                        visit.add(j)
        return answer