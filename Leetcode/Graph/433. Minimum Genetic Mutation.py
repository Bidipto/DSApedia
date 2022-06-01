#a easier version of the word ladder 1 
#look for word ladder 1 for explanations
from collections import defaultdict
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        
        adj = defaultdict(list)
        choice = ['A', 'C', 'G', 'T']
        
        bank = set(bank)
        
        if end not in bank:
            return -1
        if start not in bank:
            bank.add(start)
            
        for word in bank:
            for i in range(8):
                for letter in choice:
                    newWord = word[:i] + letter + word[i+1:]
                    if newWord in bank:
                        adj[word].append(newWord)
                        
        seen = set()
        que = deque([start])
        level = 0
        
        while que:
            level += 1
            # print(que)
            for q in range(len(que)):
                u = que.popleft()
                
                if u in seen:
                    continue
                seen.add(u)
                
                for v in adj[u]:
                    # print(u,v)
                    if v not in seen:
                        if v == end:
                            return level
                        que.append(v)
        return -1