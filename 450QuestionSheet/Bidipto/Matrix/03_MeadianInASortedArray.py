#binary search on the answer space for the meadian 
#and then calculating the number of elements that are smaller or equal to than median 
class Solution:
    def counter(self, arr, target):
        lo = 0
        hi = len(arr)-1
        while lo<=hi:
            mid = lo + (hi-lo)//2
            if arr[mid]<=target:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo  
    def median(self, mat, r, c):
        lo = 0
        hi = pow(10,4)
        half = (r * c)//2 + 1
        while lo<=hi:
            mid = lo + (hi-lo)//2
            count = 0
            for arr in mat:
                count += self.counter(arr, mid)
            # print(hi,lo,mid,count)
            if count<half:
                lo = mid+1
            else:
                hi = mid-1
        return lo