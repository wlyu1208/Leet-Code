class Solution:
    def pivotInteger(self, n: int) -> int:
        if n == 1:
            return 1

        l, r = 2, n-1
        sum_l, sum_r = 1, n

        while l <= r:
            if l == r and sum_l == sum_r:
                return l
            elif sum_l == sum_r:
                sum_l += l
                l += 1
                sum_r += r
                r -= 1
            elif sum_l < sum_r:
                sum_l += l
                l += 1
            elif sum_l > sum_r:
                sum_r += r
                r -= 1
        
        return -1