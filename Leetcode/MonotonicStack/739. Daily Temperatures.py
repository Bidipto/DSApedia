def dailyTemperatures(self, temp: List[int]) -> List[int]:
    #seems like a monotonic and a back to front trvesal question 
    #increasing stack ie highest values in the bottom
    N = len(temp)
    arr = [0]*N
    stack = []
    
    for i in range(N-1,-1,-1):
        currTemp = temp[i]
        while stack and stack[-1][0]<=currTemp:
            stack.pop()
        if stack:
            arr[i] = stack[-1][1]-i
        stack.append([currTemp,i])
            
    return arr