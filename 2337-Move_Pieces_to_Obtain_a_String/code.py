class SmallestInfiniteSet:

    def __init__(self):
        self.visits = [False] * 1001

    def popSmallest(self) -> int:
        for i in range(len(self.visits)):
            if i == 0 or self.visits[i]:
               continue
            else:
                self.visits[i] = True
                print("pop", i)
                return i

    def addBack(self, num: int) -> None:
        self.visits[num] = False


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
