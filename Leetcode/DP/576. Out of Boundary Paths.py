# 576. Out of Boundary Paths

def findPaths(self, M: int, N: int, maxMove: int, m: int, n: int) -> int:
        #simple dfs with cache with postion and number of moves remainin
        #we return the number of out of boundary point for each call
        self.mod = pow(10,9)+7
        q = deque([(m,n)])
        
        @cache
        def magic(x, y, moves):
            if moves == 0:
                return 0
            
            res = 0
            
            for m,n in (x+1,y),(x-1,y),(x,y-1),(x,y+1):
                if 0<=m<=M-1 and 0<=n<=N-1:
                    res += magic(m,n,moves-1)%self.mod
                else:
                    res += 1
            
            return res%self.mod
                            
        return magic(m,n,maxMove)