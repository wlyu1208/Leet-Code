from math import log
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False 
        
        calc_n = log(n) / log(4)
        
        if calc_n.is_integer():
            return True
        else:
            return False


from math import log, floor, ceil
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        
        if floor(log(n, 4)) == ceil(log(n, 4)):
            return True
        else:
            return False