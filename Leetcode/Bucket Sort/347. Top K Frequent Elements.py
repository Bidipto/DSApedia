from collections import Counter 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #walla bucket sort O(n) time 
        
        c = Counter(nums)
        
        bucket = [[] for q in range(len(nums)+1)]
        
        for key in c:
            bucket[c[key]].append(key)
            
        res = []
            
        for i in range(len(nums),-1,-1):
            #traversing the elements in i freq 
            for ele in bucket[i]:
                res.append(ele)
                k -= 1
                if not k:
                    return res