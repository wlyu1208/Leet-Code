class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        counter = Counter(words[0])
        n = len(words)

        for i in range(1, n):
            counter &= Counter(words[i])
        
        return list(counter.elements())