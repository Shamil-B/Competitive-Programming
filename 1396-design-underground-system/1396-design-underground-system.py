class UndergroundSystem:

    def __init__(self):
        self.checks = {}
        self.total_travel_time = defaultdict(int)
        self.total_travels = defaultdict(int)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checks[str(id)] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.checks[str(id)]
        self.total_travels[start_station + "to" + stationName] += 1
        self.total_travel_time[start_station + "to" + stationName] += (t - start_time)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.total_travel_time[startStation + "to" +  endStation] / self.total_travels[startStation + "to" + endStation]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)