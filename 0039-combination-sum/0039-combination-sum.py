class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        answer = []
        comb = []

        def backtrack(idx, remain):
            if remain == 0:
                answer.append(comb.copy())
                return
            
            for i in range(idx, len(candidates)):
                c = candidates[i]
                if c > remain:
                    break
                comb.append(c)
                backtrack(i, remain - c)
                comb.pop()

        backtrack(0, target)

        return answer