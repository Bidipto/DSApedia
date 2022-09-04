# 846. Hand of Straights
# we have to check if gorups of consecutive k elements exists

def isNStraightHand(self, nums: List[int], k: int) -> bool:
    c = collections.Counter(nums)
    N = len(nums)
    
    if N%k:
        return False 
    
    size = N//k
    
    for i in range(size):
        key = min(c)
        for val in range(key,key+k):
            if val not in c:
                return False
            else:
                c[val] -= 1
                if c[val] == 0: del c[val]
        # print(c)
    return True
        