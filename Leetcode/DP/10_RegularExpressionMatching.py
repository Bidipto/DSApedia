# 10. Regular Expression Matching
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
        #if i is out of bounds but j is not, its possible that we have a * after j
        #A/C question if there is a "*" we can have zero repetitions of the previous character
        
        if (i,j) in dp.keys():
            return dp[(i,j)]
        
        temp = False
        #even if the match is false we can skip that character in j if its followed by a "*"
        #we check for i<len(S) because if i is out of bounds we can skip that character if j is followed by a "*"
        match = ( i<len(s) and (s[i] == p[j] or p[j] == "."))
        #the only trick of the questions is to deal with "*"
        if (j+1)<len(p) and p[j+1] == "*":
            #its like nottake and take, (i,j+2) means not take
            # magic(i+1,j) means take, and we can do it only when we have a match 
            temp = magic(i,j+2) or (match and magic(i+1,j))
        elif match:
            temp = magic(i+1,j+1)
        
        dp[(i,j)] = temp
        return dp[(i,j)]
    
    return magic(0, 0)