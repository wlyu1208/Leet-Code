class MinStack:

    def __init__(self):
        self.array = []
        

    def push(self, val: int) -> None:
        self.array.append(val)

    def pop(self) -> None:
        self.array.pop()

    def top(self) -> int:
        return self.array[-1]

    def getMin(self) -> int:
        return min(self.array)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()