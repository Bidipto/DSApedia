#when we have to just return True if there exists a triplet else false
def find3Numbers(self, nums, n, X):
    nums.sort()
    result=[]
    for i in range(len(nums)-2):
        if i>0 and nums[i]==nums[i-1]:
            continue
        left=i+1
        right=len(nums)-1
        while right>left:
            curr=nums[i]+nums[left]+nums[right]
            #print(curr,nums[i],nums[left],nums[right])
            if curr>X:
                right-=1
            elif curr<X:
                left+=1
            else:
                return True
    return False
#when we have to actually return a list of the possible triplets
def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    result=[]
    for i in range(len(nums)-2):
        if i>0 and nums[i]==nums[i-1]:
            continue
        left=i+1
        right=len(nums)-1
        while right>left:
            curr=nums[i]+nums[left]+nums[right]
            #print(curr,nums[i],nums[left],nums[right])
            if curr>0:
                right-=1
            elif curr<0:
                left+=1
            else:
                result.append([nums[i],nums[left],nums[right]])
                while right>left and nums[left]==nums[left+1]:
                    left+=1
                while right>left and nums[right]==nums[right-1]:
                    right-=1
                left+=1
                right-=1
    return result