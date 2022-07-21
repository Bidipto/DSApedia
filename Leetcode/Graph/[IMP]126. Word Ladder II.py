#IMPORTANT👌💖
#similar to the word ladder part 1
#important question learnt a lot 
#see eord ladder solutin first 
from collections import defaultdict
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        if beginWord not in wordList:
            wordList.append(beginWord)
        pattern = defaultdict(list)
        adj = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                # print(word,word[:i] + '#' + word[i+1:])
                pattern[word].append(word[:i] + '#' + word[i+1:])
                adj[word[:i] + '#' + word[i+1:]].append(word)
        # print(pattern,adj)       
        seen = set()
        #it the que we use a node,path pair to keep track of the path 
        que = deque([(beginWord,[beginWord])])
        level = 1
        res = []
        flag = True
        
        while que and flag:
            level += 1
            temp = set()
            # print(que)
            for q in range(len(que)):
                u,lst = que.popleft()
                # state = (u,lst)
                if u in seen:
                    continue
                #we have to use a temp seen because if we come across the
                #node in the same level the algo with temp seen would 
                #not go through the second path 
                temp.add(u)
                
                for pat in pattern[u]:
                    for v in adj[pat]:
                        if v not in seen:
                        # print(u,v)
                            if v == endWord:
                                flag = False
                                res.append(lst + [v])
                            else:
                                que.append((v,lst+[v]))
            seen.update(temp)
        return res