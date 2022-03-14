def getMinDiff(self, arr, n, k):
    arr.sort()
    #tmin and tmax are temporary max and min variables ie the ends
    #there would be a specific point int the sorted bofore which we will only add k 
    #and after that we will only substract k
    #in the for loops we are searching for the specific pair and then we will compare with the
    #existing temp maxx and minn
    
    tmin = arr[0] + k
    tmax = arr[n - 1] - k
    ans = abs(arr[n-1]-arr[0])
    
    for i in range(1, n):
        tempmin = min(tmin, arr[i] - k) 
        tempmax = max(tmax, arr[i-1] + k)
        if tempmin<0:
            continue
        # print(ans,tempmin,tempmax)
        ans = min(ans, tempmax - tempmin)
    
    return ans