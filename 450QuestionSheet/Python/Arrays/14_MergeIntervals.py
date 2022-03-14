def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort()
    res = []
    temps = intervals[0][0]
    tempe = intervals[0][1]
    for i in range(1, len(intervals)):
        s = intervals[i][0]
        e = intervals[i][1]
        #there are three cases:
        #one where it extends the temp interval, we change the tempend
        #two jaha it just overlaps with the temp interval, and we do nothing
        #three where its completely outside, we append the current and make the present interval the new temp interval
        if tempe >= s:
            if e >= tempe:
                tempe = e
        else:
            res.append([temps, tempe])
            temps = s
            tempe = e
    res.append([temps, tempe])
    return res
                