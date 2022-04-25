# 1423. Maximum Points You Can Obtain from Cards
def maxScore(self, arr : List[int], k: int) -> int:
    #we have K number of elements to take 
    #0.....k from to start and also 0......k from end
    start = sum(arr[:k])
    end = 0
    res = start 
    for i in range(1,k+1):
        end += arr[-i]
        start -= arr[k-i]
        res = max(res, end+start)
    return res