class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        c = Counter([int(i) for i in str(n)])
        
        cur_n, i = 0, 0
        while n <= 10**9:
            cur_n = 2**i
            
            cur_c = Counter([int(i) for i in str(cur_n)])
            
            if cur_c == c:
                return True
            if len(str(cur_n)) > len(str(n)):
                return False
            
            i += 1
        return False
