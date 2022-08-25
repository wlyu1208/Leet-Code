class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        char_count = dict()
        
        for char in magazine:
            if char not in char_count:
                char_count[char] = 1
            else:
                char_count[char] += 1
        
        for ran_char in ransomNote:
            if ran_char not in char_count.keys():
                return False
            else:
                char_count[ran_char] -= 1
        
        for mag_k, mag_v in char_count.items():
            if mag_v < 0:
                return False
        
        return True
