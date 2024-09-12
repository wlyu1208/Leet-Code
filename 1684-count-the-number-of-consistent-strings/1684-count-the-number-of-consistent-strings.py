class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        _set = set(allowed)
        
        cnt = 0

        for w in words:
            if all(_c in _set for _c in w):
                cnt += 1
    
        return cnt