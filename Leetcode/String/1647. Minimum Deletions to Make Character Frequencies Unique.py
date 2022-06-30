# 1647. Minimum Deletions to Make Character Frequencies Unique

def minDeletions(self, s: str) -> int:
    #we can only delete and not append 
    c = collections.Counter(s)
    freqs = collections.Counter(c.values())
    res = 0
    maxx = max(freqs)
    # print(freqs,maxx)
    for val in range(maxx,0,-1):
        freq = freqs[val]
        # print(val,freq)
        if freq > 1:
            res += (freq-1)
            freqs[val-1] += (freq -1)
        # print(freqs,res)
    # print(freqs)
    return res

def minDeletions2(self, s: str) -> int:
    counter = Counter(s)
    #track rakhenge the least max freq that missing and lower then the crash
    #ek while loop se ho jayega
    freqlist = sorted(counter.values(), reverse = True)
    freqset = set(freqlist)
    missing = freqlist[0]
    temp = freqlist[0]
    res = 0 
    # print(freqlist)
    for i in freqlist[1:]:
        # print(temp,i,freqset)
        if i == temp:
            while missing in freqset or missing > temp:
                missing -= 1
            # print(missing)
            res += (temp-missing)
            #if its zero we dont add it
            if missing:
                freqset.add(missing)
        else:
            temp = i
    return res