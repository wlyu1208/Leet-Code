class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_dict = defaultdict(list)
        t_dict = defaultdict(list)
        
        for i, c in enumerate(s):
            s_dict[c].append(i)
        
        for i, c in enumerate(t):
            t_dict[c].append(i)
        
        for s_c, t_c in zip(s, t):
            if s_dict[s_c] != t_dict[t_c]:
                return False
        return True
        