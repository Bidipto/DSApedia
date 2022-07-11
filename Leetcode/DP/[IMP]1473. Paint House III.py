# 1473. Paint House III
# related to best time to buy and sell stock four 

def minCost(self, houses: List[int], cost: List[List[int]], M: int, N: int, target: int) -> int:
    dp={}
    
    def magic(i,last,target):
        if target<0: return -1
        if i == M:
            if not target: return 0
            else: return -1
            
        if (i,last,target) in dp: return dp[(i,last,target)]
        
        #check if already colored or not 
        if houses[i]:
            if houses[i] == last:
                res = magic(i+1,houses[i],target)
            else:
                res = magic(i+1,houses[i],target-1)
        #if not we try all colours 
        else:
            res = math.inf
            for j in range(1, N + 1):
                if j == last:
                    temp = magic(i+1,j,target)
                else:
                    temp = magic(i+1,j,target-1)
                
                if temp != -1:
                    res = min(res,cost[i][j-1] + temp)
        # print(i,last,target,res)
        if res == math.inf: res = -1
            
        dp[(i,last,target)] = res
        return res
        
    return magic(0,0,target)
    