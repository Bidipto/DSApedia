def canReach(self, s: str, minn: int, maxx: int) -> bool:
    #for each 0 we can reach we will convert it to a 2
    #and for each sliding window we will keep a counter for number of 2s
    
    #if count2>0 we will change that index to 2
    
    N = len(s)
    if s[-1] != "0" or N<=minn:
        return False
    
    test = [False]*N
    test[-1] = True
    
    last = N-minn
    sliding = deque()
    size = maxx-minn+1
    count = 0
    
    for i in range(last-1, -1, -1):
        sliding.appendleft(i+minn)
        
        if test[i+minn]:
            count += 1
        
        if len(sliding)>size:
            j = sliding.pop()
            var = test[j]
            # print(var, j)
            if var == True:
                count -= 1
                
        if count>0 and s[i]=="0":
            test[i] = True
            
        # print(sliding, test, count)
    
    return test[0]