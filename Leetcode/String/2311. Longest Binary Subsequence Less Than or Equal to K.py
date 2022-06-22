# the most valuable digit in a binary is the left most 1
# if we have the option to remove a digit and minimize the binary number
# we should remove the first 1 from left 
def longestSubsequence(self, s: str, k: int) -> int:
    summ = int(s,2)
    currLen = len(s)
    N = len(s)
    
    for i,val in enumerate(s):
        # print(summ,N)
        if summ<=k:
            return currLen
        elif val == '0':
            continue
        else:
            summ -= pow(2,N-i-1)
            currLen -=1
    
    if summ<=k:
        return N