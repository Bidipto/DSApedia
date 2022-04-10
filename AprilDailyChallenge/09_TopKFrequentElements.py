# i remember i had a headache while i had to solve this the first time
# quite a bit of progress i would say 
# used a heap to store the number of elements and the element
from collections import Counter 
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = Counter(nums)
        heap = []
        for i in dic:
            heap.append([-dic[i],i])
        heapq.heapify(heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res

#my approach in novmber lol
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    dt={}
    lstkey,lstval,ans=[],[],[]
    for i in nums:
        if i in dt.keys():
            dt[i]+=1
        else:
            dt[i]=1
    print(dt)
    for i in sorted (dt.keys()):
        lstkey.append(i)
        lstval.append(dt[i])
    for i in range(0,k):
        m=max(lstval)
        index=lstval.index(m)
        ans.append(lstkey[index])
        lstkey.pop(index)
        lstval.pop(index)
    return ans