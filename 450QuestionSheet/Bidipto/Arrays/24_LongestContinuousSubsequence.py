# a really good approach using dict
# lot to learn and msut for review 
def findLongestConseqSubseq(self,arr, N):
    #the start dic contain the starting element as key and end as valuse
    #where as the end dic contain the last element as key and start as value
    start = {}
    end = {}
    res = 1
    #there can be four cases:
    #an element is discovered which adds for front to a subseq
    #an ele whichs add to the end
    #an element which joins two existing subseq
    #a loner element
    for i in arr:
        if i+1 in start:
            if i-1 in end:
                #the third cassse, joining
                s = end.pop(i-1)
                e = start.pop(i+1)
                end[e] = s
                start[s] = e
                res = max(res, e - s + 1)
            else:
                #second case just adds to the bach
                e = start.pop(i+1)
                start[i] = e
                end[e] = i
                res = max(res, e - i + 1)
        elif i-1 in end:
            #first case where it adds to the end ie extends, eg 2 is found and 1 already exists
            s = end.pop(i-1)
            end[i] = s
            start[s] = i
            res = max(res, i - s + 1)
        elif i not in start and i not in end:
            #loner element
            start[i] = i
            end[i] = i
            
    return res