class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        spaces = []
        last = 0
        for s, e in zip(startTime, endTime):
            spaces.append(s - last)
            last = e
        spaces.append(eventTime - last)

        total = sum(spaces[:k+1])
        max_val = total

        for i in range(k+1, len(spaces)):
            total -= spaces[i-(k+1)]
            total += spaces[i]
            max_val = max(max_val, total)
        
        return max_val