def maxChunksToSorted(self, arr: List[int]) -> int:
    #used the concept of windows
    N = len(arr)
    sarr = sorted(arr)
    
    d = collections.defaultdict(collections.deque)
    
    for i,val in enumerate(sarr):
        d[val].append(i)
    

    pairs = []
    
    for i,val in enumerate(arr):
        pos = d[val].popleft()
        pairs.append(sorted([i,pos]))
        
    res = 1
    pairs.sort()
    
    # print(pairs)
    tstart = pairs[0][0]
    tend = pairs[0][1]
    
    for start,end in pairs:
        if start > tend:
            res += 1
            tstart = start 
            tend = end 
        elif end > tend:
            tend = end 
            
    return res