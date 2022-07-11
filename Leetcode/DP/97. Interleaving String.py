# 97. Interleaving String

from collections import Counter
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = {}
        N = len(s1)
        M = len(s2)
        
        
        
        def magic(i,n,m):
            if i == len(s3):
                if n == N and m == M:
                    return True
                else: return False
            
            if (i,n,m) in dp:
                return dp[(i,n,m)]
            
            temp = False 
            flag = False
            
            val = s3[i]
            if m<M and s2[m] == val:
                flag = True
                temp = temp or magic(i+1,n,m+1)
            if n<N and s1[n] == val:
                flag = True
                temp = temp or magic(i+1,n+1,m) 
            
            if not flag:
                return False 
            
            dp[(i,n,m)] = temp
            return dp[(i,n,m)]
            
        return magic(0,0,0)