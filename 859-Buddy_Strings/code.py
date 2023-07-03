class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        if s == goal:
            _set = set()

            for c in s:
                if c in _set:
                    return True
                else:
                    _set.add(c)
        
        pair = list()

        for a, b in zip(s, goal):
            if a != b:
                pair.append((a, b))
        
        for a, b in pair:
            if (b, a) in pair and len(pair) == 2:
                return True
        return False
