# 2055. Plates Between Candles

def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
    #we store the running sum,the postion of the last plate and the next plate
    #came up after quite a bit of brain storming 
    pre = 0
    preplate = -1
    nxtplate = -1
    temp = 0
    
    N = len(s)
    
    running = [0]*N
    
    for i,curr in enumerate(s):
        if curr == "|":
            preplate = i
            pre = pre + temp
            temp = 0
        else:
            temp += 1
        running[i] = [pre,preplate,-1]
        
    for i,curr in enumerate(s[::-1],1):
        if curr == "|":
            nxtplate = N-i
        running[-i][2] = nxtplate
        
    
    # print(running)
    M = len(queries)
    res = []
    
    for start,end in queries:
        # print(running[start][2],running[end][1])
        if running[start][2]>=running[end][1]:
            res.append(0)
        else:
            res.append(running[running[end][1]][0]-running[running[start][2]][0])
    return res
