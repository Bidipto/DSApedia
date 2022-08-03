def distributeCookies(self, arr: List[int], k: int) -> int:
    #try all possible ways
    #little pruning using nos, 
    # where we cap the max number of cookies a student can recieve 
    curr = [0 for q in range(k)]
    nos = [0 for q in range(k)]
    N = len(arr)
    maxx = N-k+1
    # print(curr)
    self.res = math.inf 
    
    
    def magic(i,curr):
        if i == N:
            self.res = min(max(curr),self.res)
            return
                
        for j in range(k):
            # print(j,i,curr)
            if nos[j] < maxx:
                curr[j] += arr[i]
                nos[j] += 1
                
                magic(i+1, curr)
                
                nos[j] -= 1
                curr[j] -= arr[i]
            
    magic(0,curr)
    
    return self.res