class Solution:
    def minimumSum(self, num: int) -> int:
        digit_list = [char for char in str(num)]
        sorted_list = sorted(digit_list)
        return int(sorted_list[0] + sorted_list[2]) + int(sorted_list[1] + sorted_list[3])

