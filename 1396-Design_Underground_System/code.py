class UndergroundSystem:

    def __init__(self):
        self._in = dict()
        self.total = dict()

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self._in[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        s_in, s_t = self._in[id]

        route = (s_in, stationName)
        total_t = t - s_t
        if route not in self.total:
            self.total[route] = (total_t, 1)
        else:
            prev_t, prev_cnt = self.total[route]
            self.total[route] = (prev_t + total_t, prev_cnt + 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        t, cnt = self.total[(startStation, endStation)]
        return float(t / cnt)
