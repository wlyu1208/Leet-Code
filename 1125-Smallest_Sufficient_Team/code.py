class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        n = len(req_skills)

        index = {skill:i for i, skill in enumerate(req_skills)}

        dp = {0: list()}

        for i, p in enumerate(people):
            people = 0

            for skill in p:
                people |= 1 << index[skill]
            
            for pre, team in list(dp.items()):
                update = people | pre

                if update == pre:
                    continue
                
                if update not in dp or len(dp[update]) > len(team) + 1:
                    dp[update] = team + [i]
        
        return dp[(1<<n)-1]

        print(index)
