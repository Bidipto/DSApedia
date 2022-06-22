#we sort the intervals then check if the start is before the current end, if its bfore the previous end 
#we remove the interval with the end which is nearer
def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    intervals.sort()
    tempe = intervals[0][1]
    for [s,e] in intervals[1:]:
        if s < tempe:
            counter += 1
            tempe = min(tempe, e)
        else:
            tempe = e
    return counter 