# lps in kmp algorithm
def lps(s):
    arr = [0]*len(s)
    prev = 0
    i = 1
    while i<len(s):
        if s[prev] == s[i]:
            arr[i] = prev + 1
            prev += 1
            i += 1
        else:
            if prev == 0:
                i += 1
                #default meh hi zero ha
            else:
                prev = arr[prev-1]
        print(arr,prev,i)
    return arr[-1]

s = "acccbaaacccbaac"
print(lps(s))

#only way to pass gfg question 
#by searching for the first character and the trying 
def lpsgfg(self, s):
    firstChar = s[0]
    indexOfNextF = 0
    lenS = len(s)
    while indexOfNextF <= lenS-1:

        indexOfNextF = s.find(firstChar, indexOfNextF+1)
        if indexOfNextF != -1:
            if s[:lenS-indexOfNextF] == s[indexOfNextF:]:
                return lenS - indexOfNextF
        else:
            return 0

    return 0