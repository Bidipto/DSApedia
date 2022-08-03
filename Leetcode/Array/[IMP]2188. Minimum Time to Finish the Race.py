def minimumFinishTime(self, tires: List[List[int]], time: int, laps: int) -> int:
    N = len(tires)
    total = [0]*N
    minn = []
    
    while True:
        for i in range(N):
            total[i] += tires[i][0]
            tires[i][0] *= tires[i][1]
        minn.append(min(total))
        #when the minn cost of doing one lap while changeing tire is lesser then
        #the current min lap time we break 
        if minn[-1] > time + minn[0]:
            break
            
    # print(minn)
    dp = [math.inf] * laps
    
    for i in range(laps):
        for j in range(len(minn)):
            if i-j-1<0:
                dp[i] = min(dp[i],minn[j])
                break
            else:
                dp[i] = min(dp[i],minn[j]+time+dp[i-j-1])
                
    return dp[-1]