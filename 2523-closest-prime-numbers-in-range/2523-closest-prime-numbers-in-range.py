class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        pool = [True] * (right + 1)
        pool[0] = pool[1] = False

        for i in range(2, int(right**0.5)+1):
            if pool[i]:
                for j in range(i*i, right + 1, i):
                    pool[j] = False
        
        primes = [i for i in range(left,right+1) if pool[i]]

        if len(primes) == 1:
            return [-1, -1]

        _min = 10**7
        answer = [-1, -1]

        for i in range(1, len(primes)):
            _gap = primes[i] - primes[i-1]
            if _gap < _min:
                _min = _gap
                answer = [primes[i-1], primes[i]]
        
        return answer

