# 763. Partition Labels

def partitionLabels(self, s: str) -> List[int]:
    #for every alphabhet we need to keep the last occurance of the letter in out window 
    lastPos = {val:i for i,val in enumerate(s)}
    last = lastPos[s[0]]
    res = list() 
    counter = 0 
    for i,val in enumerate(s):
        counter += 1
        last = max(lastPos[val],last)
        if last == i:
            res.append(counter)
            counter = 0
    return res