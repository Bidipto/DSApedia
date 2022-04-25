#O(n) approach is kinda hard to come up with 
def firstMissingPositive(self, nums: List[int]) -> int:
        #since the negative numbers are useless and cause a problem if we try to use
        #to use the negation meathod we convert the negs to zeros
        for i in range(len(nums)):
            if nums[i]<0:
                nums[i] = 0
        
        #now we negate the values at indexes only a simple cache
        #what if we find a 2 and at 2 index there is a 0
        #we cant convert it to a -1 cause that would mwan we have seen a -1
        #notice how the answer space is 1....len(Arr)
        #therefore -len(arr) is a safe conversion for zeros
        #also keep in mind if to negate on in bound index
        
        N = len(nums)
        for i in range(N):
            num = abs(nums[i])-1 
            #checking for in bounds and if already not negated
            if 0<=num<N: 
                if nums[num]>0 :
                    nums[num] *= -1
                elif nums[num] == 0:
                    nums[num] = -N-1
        # print(nums)
        # if all 1.....N are present then all element would be negated and ans would be N+1
        for i in range(N):
            if nums[i]>=0:
                return i+1
        else:
            return N+1