class Solution:
    def trip_fib(self, n, track):
        if n in track:
            return track[n]
        else:
            track[n] = self.trip_fib(n-1, track) + self.trip_fib(n-2, track) + self.trip_fib(n-3, track)
            return track[n]
    
    def tribonacci(self, n: int) -> int:
        answer = 0
        track = {}
        track[0] = 0
        track[1] = 1
        track[2] = 1
        answer = self.trip_fib(n, track)
        return answer
        
