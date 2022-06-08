class Solution:
    def removePalindromeSub(self, s: str) -> int:
        # if len is 0 then its just 0
        if len(s) == 0:
            return 0
        # if len is 1 then its palindromic so its 1
        elif len(s) == 1:
            return 1
        # if palindromic, answer is always 1. if not answer is always 2 since 
        else:
            if s == s[::-1]:
                return 1
            else:
                return 2
