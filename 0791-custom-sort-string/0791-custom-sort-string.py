class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s_counter = Counter(s)

        result = ''

        for char in order:
            if char in s_counter:
                result+=char*s_counter[char]
                del s_counter[char]
        
        for char in s_counter:
            result += char * s_counter[char]

        return result