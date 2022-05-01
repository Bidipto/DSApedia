#3-d dp,just dono robot ek saath chod diye
def cherryPickup(self, arr: List[List[int]]) -> int:
    N = len(arr[0])
    M = len(arr)
    dp = [[[-1 for c in range(N)] for b in range(N)] for a in range(M)]
    #dp[row][column1][column2]
    
    def magic(m, n1, n2):
        if dp[m][n1][n2] != -1:
            return dp[m][n1][n2]
        
        cherry = arr[m][n1] + arr[m][n2] if n1 != n2 else arr[m][n1]
        
        if m == M-1:
            return cherry
        
        temp = -math.inf
        for j1,j2 in product([n1-1,n1,n1+1],[n2-1,n2,n2+1]):
            # print(m,j1,j2)
            if 0<=j1<N and 0<=j2<N:
                temp = max(temp, magic(m+1,j1,j2))
                
        dp[m][n1][n2] = cherry + temp
        return dp[m][n1][n2]
    
    return magic(0,0,N-1)