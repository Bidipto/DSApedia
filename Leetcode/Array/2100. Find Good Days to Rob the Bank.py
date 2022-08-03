def goodDaysToRobBank(self, arr: List[int], time: int) -> List[int]:
        #just some pre computation makes this super easy
        N = len(arr)
        
        pre = [-1 for i in range(N)]
        post = [-1 for i in range(N)]
        
        pre[0] = 0
        
        temp = 0
        
        for i in range(1,N):
            if arr[i-1]>=arr[i]:
                temp += 1
            else:
                temp = 0
            pre[i] = temp
            
        post[-1] = 0
        temp = 0
        
        for i in range(N-2,-1,-1):
            if arr[i]<=arr[i+1]:
                temp += 1
            else:
                temp = 0
            post[i] = temp
        
        print(pre,post)
        res = []
        
        
        
        for i in range(N):
            if pre[i]>=time and post[i]>=time:
                res.append(i)
                
        return res