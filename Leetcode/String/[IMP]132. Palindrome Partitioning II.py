# 132. Palindrome Partitioning 
def minCut(self, s: str) -> int:
        N = len(s)
        #for every postiion res[i] countain the min number of cuts for i-1 th postion
        #therefore res[0] will always be 0 and res[N] will return the ressult
        #we will take every postion as the starting point as odd and even palindorme
        #and in that process we will minimise the result at each end point of the palindrome
        
        #imp we will update the end pos of each positon 
        res = [i for i in range(-1,N)]
        
        for i in range(N):
            #odd palindromes:
            first, last = 0, 0
            while i-first>=0 and i+last<N and s[i-first] == s[i+last]:
                res[i+last+1] = min(res[i+last+1],1 + res[i-first])
                first += 1
                last += 1
            
            #even palindromes:
            if i+1<N and s[i] == s[i+1]:
                first, last = 0, 1 
                while i-first>=0 and i+last<N and s[i-first] == s[i+last]:
                    # print(i-first, i+last)
                    res[i+last+1] = min(res[i+last+1],1 + res[i-first])
                    first += 1
                    last += 1
        #             print( s[i-first],i-first,s[i+last],i+last)
        #     print(res, i)
        # print(res) 
        return res[N]