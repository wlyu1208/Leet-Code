class Solution:
    def coloredCells(self, n: int) -> int:
        # n   1 2 3 4   5
        # 증가 1 4 8 12, 16, 20, 24, .....
        # 답   1 5 13 25, 
    # """
    # 1 + 4 + 8 + 12 + 16 + .... 4(i-1)
    # 1 + 4(1 + 2 + 3 + 4 ..... + i-1)
    # """
        return 1 + 4*sum(range(1, n))

