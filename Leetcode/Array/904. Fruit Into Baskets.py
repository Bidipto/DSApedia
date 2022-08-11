def totalFruit(self, s: List[int]) -> int:
    #maintainin the counter of fruits that i have
    #two pointer technique
    c = collections.Counter()
    c[s[0]] = 1
    
    start = 0
    res = 1
    
    for end in range(1,len(s)):
        # print(start,end,c, c.most_common()[0][1])
        c[s[end]] += 1
        while len(c)>2:
            c[s[start]] -= 1
            if c[s[start]] == 0:
                del c[s[start]]
            start += 1
        res = max(res,end-start+1)
    return res