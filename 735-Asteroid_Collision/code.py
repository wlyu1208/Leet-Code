class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for meteor in asteroids:
            while stack and stack[-1] > 0 > meteor:
                if stack[-1] < abs(meteor):
                    stack.pop()
                    continue
                if stack[-1] == abs(meteor):
                    stack.pop()
                break
            else:
                stack.append(meteor)
        return stack
        
