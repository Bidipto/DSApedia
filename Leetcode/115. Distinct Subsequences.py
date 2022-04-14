def numDistinct(self, s: str, t: str) -> int:
    dp = {}
    #i is pointer for s and j is pointer for t
    S = len(s)
    T = len(t)
    def magic(i,j):
        #if j is pointing at the end, therefore we have sucessfully found a string  
        if j == T:
            return 1
        # if i is overbound, we cant go only further
        if i == S:
            return 0
        
        if (i,j) in dp:
            return dp[(i,j)]
        
        #when there is a match we have an option to take and not take
        if s[i] == t[j]:
            dp[(i,j)] = magic(i+1,j+1) + magic(i+1,j)
        #when there is no match we cant take that char in s
        else:
            dp[(i,j)] = magic(i+1,j)
            
        return dp[(i,j)]
    return magic(0, 0)