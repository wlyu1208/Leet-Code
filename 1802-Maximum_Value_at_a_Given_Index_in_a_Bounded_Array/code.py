class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        maxSum -= n # possible max_n = maxSum - (1 * n) -> [1, 1, 1, ...]

        def check(_mid):
            left = min(_mid - 1, index)
            right= min(_mid - 1, n - index - 1)

            left_s = (_mid - 1 + _mid - left) * left // 2
            right_s = (_mid - 1 + _mid - right) * right // 2

            sum_s = left_s + right_s + _mid

            return sum_s <= maxSum
        
        l, r = 1, 10**9

        while l < r:
            mid = (l + r) // 2
            if check(mid):
                l = mid + 1
            else:
                r = mid
        return l
