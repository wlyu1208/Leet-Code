class MyHashSet:

    def __init__(self):
        self.array = set()

    def add(self, key: int) -> None:
        self.array.add(key)

    def remove(self, key: int) -> None:
        if key in self.array:
            self.array.remove(key)

    def contains(self, key: int) -> bool:
        if key in self.array:
            return True
        else:
            return False
