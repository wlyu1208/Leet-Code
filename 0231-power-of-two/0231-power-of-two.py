import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # if n <= 0: return False
        # elif n == 1: return True
        # elif math.log2(n).is_integer(): return True
        # return False

        return n > 0 and n & (n-1) == 0