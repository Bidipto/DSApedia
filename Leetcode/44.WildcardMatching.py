# 44. Wildcard Matching
#optimized the below solution a little bit
def isMatch(self, s: str, p: str) -> bool:
    dp = {}
    def magic(i,j):
        #if i is out of bounds along with j,
        #we return cause its matched successfully
        if i>=len(s) and j>=len(p):
            return True
        #if j is out of bounds and not i, there is no way we can match
        if j>=len(p):
            return False
        
        #a little trick is to deal with "*" and suprised with the optimiazation
        if p[j] == "*" and (i,"*") in dp.keys():
            return dp[(i,"*")]
        if (i,j) in dp.keys():
            return dp[(i,j)]
        
        temp = False
        match = ( i<len(s) and (s[i] == p[j] or p[j] == "?"))
        #the only trick of the questions is to deal with "*"
        if p[j] == "*":
            #take and not take
            #magic(i+1,j) means take
            #magic(i,j+1) means not take
            #also while taking we need to ensure i is not out of bounds
            dp[(i,"*")] = magic(i,j+1) or (i<len(s) and magic(i+1,j))
            return dp[(i,"*")]
        elif match:
            temp = magic(i+1,j+1)
        
        dp[(i,j)] = temp
        return dp[(i,j)]
    
    return magic(0, 0)
# quite sililar to regular expression matching
# but kafi zada slowwwwww
def isMatch(self, s: str, p: str) -> bool:
    dp = {}
    def magic(i,j):
        #if i is out of bounds along with j,
        #we return cause its matched successfully
        if i>=len(s) and j>=len(p):
            return True
        #if j is out of bounds and not i, there is no way we can match
        if j>=len(p):
            return False
        
        if (i,j) in dp.keys():
            return dp[(i,j)]
        
        temp = False
        match = ( i<len(s) and (s[i] == p[j] or p[j] == "?"))
        #the only trick of the questions is to deal with "*"
        if p[j] == "*":
            #take and not take
            #magic(i+1,j) means take
            #magic(i,j+1) means not take
            #also while taking we need to ensure i is not out of bounds
            temp = magic(i,j+1) or (i<len(s) and magic(i+1,j))
        elif match:
            temp = magic(i+1,j+1)
        
        dp[(i,j)] = temp
        return dp[(i,j)]
    
    return magic(0, 0)

