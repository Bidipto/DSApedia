def minimumTotal(self, triangle: List[List[int]]) -> int:
    dp = {}
    def magic(m,n):
        if m == len(triangle):
            # res[0] = min(res[0],currsum)
            return 0
        
        if (m,n) in dp:
            return dp[(m,n)]
        
        temp =triangle[m][n] + min(magic(m+1,n),magic(m+1,n+1))
        
        dp[(m,n)] = temp
        return temp
    
    return magic(0,0)
            