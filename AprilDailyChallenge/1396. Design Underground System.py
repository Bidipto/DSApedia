# 1396. Design Underground System
from collections import defaultdict
class UndergroundSystem:

    def __init__(self):
        #naya sikh
        self.time = defaultdict(lambda: [0,0])
        self.travel = {}

    def checkIn(self, id: int, station: str, t: int) -> None:
        self.travel[id] = [station,t]

    def checkOut(self, id: int, station: str, t: int) -> None:
        startstation, starttime = self.travel.pop(id)
        self.time[startstation+'#'+station][0] += (t - starttime)
        self.time[startstation+'#'+station][1] += 1
    def getAverageTime(self, start: str, end: str) -> float:
        return self.time[start+'#'+end][0]/self.time[start+'#'+end][1]
