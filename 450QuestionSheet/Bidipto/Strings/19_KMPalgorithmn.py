#watch kmp algo on neetcode 
def strStr(self, haystack: str, needle: str) -> int:
    #first we have to impelement longest prefix suffix
    lps = [0]*len(needle)
    pre, i = 0, 1
    while i<len(needle):
        if needle[pre] == needle[i]:
            lps[i] = pre + 1
            pre += 1
            i += 1
        elif pre == 0:
            #lps has value 0 by default
            i += 1
        else:
            pre = lps[pre - 1]
            
    # print(lps)
    #second we have to search for the pattern
    i, j = 0, 0
    while i<len(haystack):
        if haystack[i] == needle[j]:
            i += 1
            j += 1
        elif j == 0:
            i += 1
        else:
            j = lps[j-1]
        #break statement if found:
        if j == len(needle):
            return i-j
    return -1