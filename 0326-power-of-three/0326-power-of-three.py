class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        max_3 = 3 ** 19

        return n > 0 and max_3 % n == 0