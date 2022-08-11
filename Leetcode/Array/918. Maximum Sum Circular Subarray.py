# 918. Maximum Sum Circular Subarray

def maxSubarraySumCircular(self, arr: List[int]) -> int:
    #here cuursum is take and maxi is not take
    sumarr = sum(arr)
    
    currsum=0
    maxi = arr[0]
    currsumneg = 0
    maxineg = arr[0]
    
    for i in arr:
        # print(currsum,maxi)
        currsum = i + max(0, currsum)
        maxi = max(maxi,currsum)
        currsumneg = i + min(0, currsumneg)
        maxineg = min(maxineg,currsumneg)
    
    # print(maxineg,maxi)
    #handling the sitution of when the maxineg is the entire array 
    return maxi if sumarr == maxineg else max(sumarr - maxineg, maxi)
        