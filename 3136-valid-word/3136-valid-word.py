class Solution:
    def isValid(self, word: str) -> bool:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        def check(w_s: str):
            cnt_v, cnt_w = 0, 0
            for w in w_s:
                if w.isdigit(): continue

                if w in vowels: cnt_v += 1
                if w not in vowels: cnt_w += 1

                if cnt_v >= 1 and cnt_w >= 1:
                    return True
            return False

        return len(word) >= 3 and word.isalnum() and check(word)