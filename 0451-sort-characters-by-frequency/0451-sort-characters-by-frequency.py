class Solution:
    def frequencySort(self, s: str) -> str:
        char_counts = Counter(s)

        sort_char_counts = dict(sorted(char_counts.items(), key=lambda x: x[1], reverse=True))
        ans = ""
        for k, v in sort_char_counts.items():
            ans += k * v
        
        return ans