#good logic
#look for dicussion
#its the leed version of the problem
# 696. Count Binary Substrings

#The questions calls for CONSEQUTIVE 0s and 1s
#the gfg version in the sheet requires a a easier verion of this logic
def countBinarySubstrings(self, s: str) -> int:
    curr = 0
    prev = 0
    
    res = 0
    if s[0] == "0":
        flag = False
    else:
        flag = True
    for i in s:
        if i == "0":
            if flag:
                res += min(curr,prev)
                prev = curr
                curr = 0
                flag = not flag
        else:
            if not flag:
                res += min(curr,prev)
                prev = curr
                curr = 0
                flag = not flag
        curr += 1
    res += min(curr,prev)
                
    return res 