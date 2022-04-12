# Maximum Sum Circular Subarray
def maxSubarraySumCircular(self, arr: List[int]) -> int:
        #here cuursum is take and maxi is not take
        #maxi neg is the maximum negative subarray that can be formed
        #and maxi is the maximum sum subarray in the given array 
        # therefore the answer will be the max(arraysum + maxineg, maxi)
        #maxineg is positive here
        sumarr = sum(arr)
        
        currsum=0
        maxi = arr[0]
        
        for i in arr:
            currsum = i + max(0, currsum)
            maxi = max(maxi,currsum)
            
        currsum = 0
        maxineg = -arr[0]
        
        for i in [-i for i in arr]:
            currsum = i + max(0, currsum)
            maxineg = max(maxineg,currsum)
        
        print(maxineg,maxi)
        if sumarr + maxineg == 0:
            return maxi
        else :
            return max(sumarr + maxineg, maxi)