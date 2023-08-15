class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            '{': '}',
            '[': ']',
            '(': ')'
        }
        stack = []
        starts = pairs.keys()

        for c in s:
            if c in starts:
                stack.append(c)
            else:
                if len(stack) != 0:
                    if c != pairs[stack[-1]]:
                        return False
                    else:
                        stack.pop()
                else:
                    return False

        if stack:
            return False
        return True
