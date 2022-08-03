# 692. Top K Frequent Words

from sortedcontainers import SortedList, SortedSet, SortedDict
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        #bucket sort with sortedlist 
        c = Counter(words)
        
        bucket = [SortedList() for q in range(len(words)+1)]
        
        for key in c:
            bucket[c[key]].add(key)
            
        res = []
            
        for i in range(len(words),-1,-1):
            #traversing the elements in i freq 
            for ele in bucket[i]:
                res.append(ele)
                k -= 1
                if not k:
                    return res