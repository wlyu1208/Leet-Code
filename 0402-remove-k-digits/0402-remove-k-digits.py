class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            while k > 0 and stack and digit < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(digit)

        if k > 0:
            stack = stack[:-k]

        ans = ''.join(stack).lstrip('0')
        ans = '0' if not ans else ans
        return ans