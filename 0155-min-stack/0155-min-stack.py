class MinStack:

    def __init__(self):
        self.array = []
        self.min_array = []

    def push(self, val: int) -> None:
        self.array.append(val)
        if self.min_array:
            val = min(self.min_array[-1], val)
        self.min_array.append(val)

    def pop(self) -> None:
        self.array.pop()
        self.min_array.pop()

    def top(self) -> int:
        return self.array[-1]

    def getMin(self) -> int:
        return self.min_array[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()