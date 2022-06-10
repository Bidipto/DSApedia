# use two pointers 
# keep coll and understand the problem and then find an approach

def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i = 0
        j = 0
        res = 0
        #nums[i]<=nums[j]
        # [55,10,5,4,2]
        #  i
        # [100,60,10,7,5]
        #      j  
        while i<len(nums1) and j<len(nums2):
            if nums1[i] <= nums2[j]:
                res = max(res,j-i)
                j += 1
            else:
                i += 1
        return res