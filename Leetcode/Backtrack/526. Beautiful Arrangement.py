# 526. Beautiful Arrangement
def countArrangement(self, n: int) -> int:
        #simple permutation with checks for the given condition
        s = {i for i in range(1,n+1)}
        res = [0]
        
        def magic(N,s):
            if not s:
                res[0] += 1
                return 
            
            for i in s:
                if i % N == 0 or N % i ==0:
                    magic(N+1,s - {i})
                    
        magic(1,s)
        return res[0]