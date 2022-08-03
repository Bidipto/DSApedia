# kafi sahi concept
# will make a great interview question
def canPartitionKSubsets(self, arr: List[int], k: int) -> bool:
    s = sum(arr)
    N = len(arr)
    
    if s%k or N<k:
        return False
    
    target = s/k
    
    if max(arr)>target:
        return False
    
    arr.sort(reverse = True)
    seen = [False]*len(arr)
    
    @cache
    def magic(i,k,summ,t):
        if k == 0:
            return True
        
        if summ==target:
            if k == 1: return True
            else: return magic(0,k-1,0,t)
        
        for j in range(i, len(arr)):
            if seen[j] or summ + arr[j]>target:
                continue
                
            seen[j] = True
            temp = seen[:]
            if magic(j+1,k,summ+arr[j],tuple(temp)): return True

            seen[j] = False
                
        return False
    
    return magic(0,k,0,tuple(seen))