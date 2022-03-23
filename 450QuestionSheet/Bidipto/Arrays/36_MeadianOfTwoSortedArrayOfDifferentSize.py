import math
def findMedianSortedArrays( nums1, nums2):
    A = nums1
    B = nums2
    if len(B)<len(A):
        A,B = B,A
    #in case of odd the first partition will always be smaller ie median will be
    #the first element of the second partition
    half = (len(A) + len(B))//2
    #we are doing a binary search in the smaller array
    #taki humne pata chale how many element we will take from the first array 
    lo, hi = 0,len(A) - 1
    print(lo,hi,A)
    while True:
        #i is the index of elements from the first array
        i = (lo + hi)//2
        #j is the index of elements from the larger array
        j = half - i - 2
        
        Aleft = A[i] if i>=0 else -math.inf
        Aright = A[i+1] if i+1<len(A) else math.inf
        Bleft = B[j] if j>=0 else -math.inf
        Bright = B[j+1] if j+1<len(B) else math.inf
        
        if Aleft<=Bright and Bleft<=Aright:
            #odd
            if (len(A) + len(B))%2:
                return min(Aright,Bright)
            #even
            return float(max(Aleft,Bleft) + min(Aright,Bright))/2
        #more element from A, so hume kam karna ha elements from A
        elif Aleft>Bright:
            hi = i-1
        #less elements form A, so hume zada karna ha elements from A
        else:
            lo = i+1
            

print(findMedianSortedArrays([1,2],[3,4]))