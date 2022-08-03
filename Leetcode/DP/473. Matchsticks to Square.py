# 473. Matchsticks to Square

def makesquare(self, matchsticks: List[int]) -> bool:
    value = sum(matchsticks)
    if value < 4:
        return False
    if value % 4 != 0:
        return False
    edge = value // 4
    matchsticks.sort(reverse=True)
    @cache
    def findedges(l1, l2, l3, l4, i):
        nonlocal edge
        if l1 == l2 == l3 == l4 == edge:
            return True
        if i > len(matchsticks) - 1:
            return False
        if l1 > edge or l2 > edge or l3 > edge or l4 > edge:
            return False
        return findedges(l1 + matchsticks[i], l2, l3, l4, i + 1) or findedges(l1, l2 + matchsticks[i] , l3, l4, i + 1) or findedges(l1, l2, l3 + matchsticks[i], l4, i + 1) or findedges(l1, l2, l3, l4 + matchsticks[i] , i + 1)
    return findedges(0, 0, 0, 0, 0)


def makesquare2(self, arr: List[int]) -> bool:
        #we are expected to keep tab of all the sides
        dp = {}
        N = len(arr)
        summ = sum(arr)
        
        if summ%4: 
            return False 
        
        if max(arr)>summ//4:
            return False 
        
        target = summ//4
        arr.sort(reverse=True)
        
        def magic(i,a,b,c,d):
            if a>target or b>target or c>target or d>target:
                return False
            
            if a == b == c == d == target:
                return True
            
            if i == N:
                return False
            
            if (a,b,c,d) in dp:
                return dp[(a,b,c,d)]
            
            val = arr[i]
            #a or b or c or d
            if magic(i+1,a+val,b,c,d) or magic(i+1,a,b+val,c,d) or magic(i+1,a,b,c+val,d) or magic(i+1,a,b,c,d+val):
                dp[(a,b,c,d)] = True
                return True
            else:
                dp[(a,b,c,d)] = False
                return False 
            
        return magic(0,0,0,0,0)