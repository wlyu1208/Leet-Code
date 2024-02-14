class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos, neg = [], []
        for n in nums:
            if n > 0:
                pos.append(n)
            else:
                neg.append(n)
        
        ans = []
        p_idx, n_idx = 0, 0
        for i in range(len(nums)):
            if i % 2 == 0:
                ans.append(pos[p_idx])
                p_idx += 1
            else:
                ans.append(neg[n_idx])
                n_idx += 1
        return ans