def findMaxForm(self, strs: List[str], M: int, N: int) -> int:
        Len = len(strs)
        dp = [[[- 1]*(N+1) for i in range(M+1)] for k in range(Len)]
        
        
        dic = {}
        for i,s in enumerate(strs): 
            zero, one = 0,0
            for j in s:
                if j == "0":
                    zero += 1
                else:
                    one += 1
            dic[i] = [zero,one]
        
        
        def magic(i, m, n):
            if i >= Len:
                return 0

            
            if dp[i][m][n] != -1:
                return dp[i][m][n]
            
            #take 
            zero,one = dic[i]
            # print(strs[i],zero,one)
            if m - zero >= 0 and n - one >= 0:
                take = 1 + magic(i+1,m-zero,n-one)
            else:
                #we can just return magic(i+1,m,m) but whateve
                take = 0
            
            #nottake
            nottake = magic(i+1,m,n)
            
            dp[i][m][n] = max(take,nottake)
            return dp[i][m][n]
        
        return magic(0,M,N)