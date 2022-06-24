class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        s_list = list(s)
        print(s_list)
        
        track = {}
        for l, r in pairs:
            if l not in track:
                track[l] = set()
                track[l].add(l)
                track[l].add(r)
            else:
                track[l].add(r)
        
        for cur_set in track.values():
            str_list = sorted([s_list[x] for x in cur_set])
            set_list = sorted(list(cur_set))
            
            for i in range(len(set_list)):
                cur_s = set_list[i]
                s_list[cur_s] = str_list[i]

        return "".join(s_list)
