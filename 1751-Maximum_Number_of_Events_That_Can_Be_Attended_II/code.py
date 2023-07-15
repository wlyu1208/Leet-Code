class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        @cache
        def helper(idx, last_end, count):
            if idx == n or count == k:
                return 0
            
            #skip
            best = helper(idx+1, last_end, count)

            # get
            if events[idx][0] > last_end:
                best = max(best, events[idx][2] + helper(idx + 1, events[idx][1], count + 1))

            return best
        
        n = len(events)
        events.sort()
        return helper(0, 0, 0)

