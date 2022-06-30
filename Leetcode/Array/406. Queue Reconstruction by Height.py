# 406. Queue Reconstruction by Height
#we keep track of number of people that are taller in the queue for every iteration 
from collections import defaultdict,Counter
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        freq = defaultdict(set)
        curr = {}
        lst = set()
        
        for u,v in people:
            freq[u].add(v)
            curr[u] = 0
            lst.add(u)
            
        lst = sorted(list(lst))
        que = []
        count = 0
        while len(que)!=len(people):
            for i,val in enumerate(lst):
                if curr[val] in freq[val]:
                    que.append([val,curr[val]])
                    freq[val].remove(curr[val])
                    for j in lst[:i+1]:
                        curr[j] += 1
                    break
                        
            # print(freq,curr,que)
        return que