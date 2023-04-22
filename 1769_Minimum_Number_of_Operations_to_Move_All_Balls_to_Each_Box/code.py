class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        
        for char1, char2 in zip(word1, word2):
            result += char1 + char2
        
        len1 = len(word1)
        len2 = len(word2)
        if len1 < len2:
            result += word2[len1:len2]
        elif len1 > len2:
            result += word1[len2:len1]
        
        return result
