#negating the seen elements
#catc:  doesnt work if 0 is added lol 
def findDuplicates(self, nums: List[int]) -> List[int]:
    res = []
    for i in range(len(nums)):
        if nums[abs(nums[i])-1]<0:
            res.append(abs(nums[i]))
        else:
            nums[abs(nums[i])-1] *= -1
    return res

#if its a string we can use a dictionary 
#and return the elements with ferquency more than 1