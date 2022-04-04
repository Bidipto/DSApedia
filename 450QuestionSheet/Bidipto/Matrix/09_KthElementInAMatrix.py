def kthSmallest(mat, n, k): 
    #binary search on the probable answer space
    #using a counter function to count the number of elements less then mid
    def magic(mid):
        count = 0
        for arr in mat:
            for num in arr:
                if num<=mid:
                    count += 1
                else:
                    break
        return count
    lo = 0
    hi = 10000
    while lo<=hi:
        mid = lo + (hi-lo)//2
        count = magic(mid)
        if count>=k:
            hi = mid - 1
        else:
            lo = mid + 1
    #return lo cause before the while loop break lo and hi will be the same
    #and hi is decremented by 1, threrefore lo will be the answer
    return lo