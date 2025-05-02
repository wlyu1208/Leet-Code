class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)

        forces = [0] * n
        force = 0
        for i in range(n):
            if dominoes[i] == 'L':
                force = 0
            elif dominoes[i] == 'R':
                force = n
            else:
                force = max(force-1, 0)
            forces[i] = force
        # print(forces)
        
        force = 0
        for i in range(n-1, -1, -1):
            if dominoes[i] == 'L':
                force = n
            elif dominoes[i] == 'R':
                force = 0
            else:
                force = max(force-1, 0)
            forces[i] -= force
        # print(forces)

        answer = ''

        for force in forces:
            if force == 0:
                answer += '.'
            elif force < 0:
                answer += 'L'
            else:
                answer += 'R'
        return answer