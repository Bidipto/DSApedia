# 647. Palindromic Substrings
def countSubstrings(self, s: str) -> int:
        N = len(s)
        res = N
        
        #odd:
        for n in range(N):
            t = 1
            while 0<=n-t and n+t<N and s[n-t] == s[n+t]:
                res += 1
                t += 1
                    
        #even
        for n in range(1,N):
            t = 0
            while 0<=n-t-1 and n+t<N and s[n-t-1] == s[n+t]:
                res += 1
                t += 1
                    
        return res