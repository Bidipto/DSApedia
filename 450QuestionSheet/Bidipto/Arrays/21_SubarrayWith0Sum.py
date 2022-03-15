#we have a set with the running sum
#if there is a subset with sum 0, the running sum before the last element before the subset 
#will be equal to the running sum at the lst element of the subset
#therefore that perticular running sum will exist in the set
#if the quesntion demanded the indexes of the subset we could have used a dictionary
def subArrayExists(self,arr,n):
    res = 0
    s = set()
    s.add(0)
    for i in arr:
        res += i
        if res in s: return True
        s.add(res)
    return False