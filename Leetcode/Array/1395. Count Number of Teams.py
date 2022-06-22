#read the question for a better understanding 
def numTeams(self, rating: List[int]) -> int:
    res = 0
    for i,val in enumerate(rating):
        leftLess = 0
        leftMore = 0
        rightMore = 0
        rightLess = 0
        #search in the left subwindow 
        for j in range(i):
            newVal = rating[j]
            if newVal<val:
                leftLess += 1
            else:
                leftMore += 1
        #seach in the right subwindow 
        for j in range(i+1,len(rating)):
            newVal = rating[j]
            if newVal<val:
                rightLess += 1
            else:
                rightMore += 1
                
        res += ((leftLess * rightMore)+(leftMore * rightLess))
    return res