#simple solution using a reverse for loop
def reverseWord(s):
    res=[]
    for i in range(len(s)-1,-1,-1):
        res.append(s[i])
    return "".join(res)
    
#inplace solution using a reverse function could be used as-well