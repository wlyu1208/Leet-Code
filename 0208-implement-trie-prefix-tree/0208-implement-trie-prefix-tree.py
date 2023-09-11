class Node:
    def __init__(self, key, count=0):
        self.key = key
        self.child = {}

class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, word: str) -> None:
        cur = self.head

        for c in word:
            if c not in cur.child:
                cur.child[c] = Node(c)
            cur = cur.child[c]
        cur.child['*'] = True

        self.previous = word

    def search(self, word: str) -> bool:
        cur = self.head

        for c in word:
            if c not in cur.child:
                return False
            cur = cur.child[c]
        if '*' in cur.child:
            return True
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.head
        for c in prefix:
            if c not in cur.child:
                return False
            cur = cur.child[c]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)