import sys

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        last = triangle[-1]
        
        for i in range(len(triangle)-2, -1, -1):
            cur_row = triangle[i]
            new_last = []
            for j in range(len(cur_row)):
                last_part = last[j:j+2]
                new_last.append(min(cur_row[j]+last_part[0], cur_row[j]+last_part[1]))
            last = new_last
    
        return last[0]
