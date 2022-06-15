class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        set_word = set(words)
        track = {}
        
        def check(word):
            if word not in set_word:
                return 0
            if word in track:
                return track[word]
            else:
                n = len(word)
                cur_max = -1
                for i in range(n):
                    cur_max = max(cur_max, check(word[:i] + word[i+1:])+1)
                track[word] = cur_max
            
            return cur_max
        
        for each_word in words:
            check(each_word)
            
        return max(track.values())
