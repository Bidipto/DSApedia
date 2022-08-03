#can be memonized as well we look at the possibilities at each n
def maxTaxiEarnings(self, n: int, arr: List[List[int]]) -> int:
    d = defaultdict(list)
    @cache 
    def magic(start):
        if start == n:
            return 0
        
        #not take 
        temp = magic(start+1)
        
        #take 
        for end,tip in d[start]:
            temp = max(temp, end - start + tip + magic(end))
        
        return temp
    
    for start,end,tip in arr:
        d[start].append((end,tip))

    return magic(0)