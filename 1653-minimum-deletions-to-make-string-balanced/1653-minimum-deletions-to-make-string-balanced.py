class Solution:
    def minimumDeletions(self, s: str) -> int:
        b_cnt, min_delete = 0, 0

        for c in s:
            if c == 'b':
                b_cnt += 1
            else:
                min_delete = min(min_delete + 1, b_cnt)
        
        return min_delete