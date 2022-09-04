# doing or to keep all the significant 1s anf doing xor to remove the 1s of arr[lo]
# think about it pretty good concept 

def longestNiceSubarray(self, arr: List[int]) -> int:
    res = 1 
    lo = 0
    hi = 1
    sume = arr[0]
    while hi<len(arr):
        while lo<hi and sume & arr[hi] != 0:
            sume ^= arr[lo]
            lo += 1
        res = max(res,hi-lo+1)
        sume |= arr[hi]
        hi += 1
    
    return res