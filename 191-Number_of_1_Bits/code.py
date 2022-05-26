class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        x = format(n, 'b')
        str_n = str(x.zfill(32))
        
        count = 0
        
        for i in str_n:
            if i == '1':
                count += 1
        
        return count
