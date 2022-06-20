class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        set_w = set(words)
        n = len(words)
        
        for word in words:
            cur_len = len(word)
            for j in range(1, cur_len):
                if word[-j:] in set_w:
                    set_w.remove(word[-j:])
        
        return len('#'.join(set_w)+"#")
