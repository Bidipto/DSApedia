#naive heap solution
def kthSmallest(self,arr, l, r, k):
    heapq.heapify(arr)
    for i in range(k):
        res = heapq.heappop(arr)
    return res

# an efficient solution is to use a quicksort
# leetcode question 215 find Kth Largest Element in an Array
def findKthLargest(self, nums, k):
    if len(nums)==1:
        return nums[0]
    
    temp = nums[-1]
    big = [i for i in nums if i>temp]
    equal = [i for i in nums if i==temp]
    small = [i for i in nums if i<temp]
    
    if len(big)>=k:
        return self.findKthLargest(big, k)
    elif len(big)+len(equal)>=k:
        return equal[0]
    else:
        return self.findKthLargest(small, k - len(equal) - len(big))
        