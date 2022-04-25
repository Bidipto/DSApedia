# 1647. Minimum Deletions to Make Character Frequencies Unique
def minDeletions(self, s: str) -> int:
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