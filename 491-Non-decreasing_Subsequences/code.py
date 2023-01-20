class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = list()

        def backtrack(start, seq, ans):
            if len(seq) > 1:
                ans.append(seq)
            
            visit = set()
            for i in range(start, len(nums)):
                if nums[i] in visit:
                    continue
                if len(seq) == 0 or nums[i] >= seq[-1]:
                    visit.add(nums[i])
                    next_seq= seq + [nums[i]]
                    backtrack(i+1, next_seq, ans)


        backtrack(0, list(), ans)
        return ans
