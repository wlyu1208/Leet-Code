class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        
        binaries = bin(n)
        bins = binaries[2:]
        cnt_1 = bins.count('1')

        if cnt_1 > 1:
            return False
        
        return True