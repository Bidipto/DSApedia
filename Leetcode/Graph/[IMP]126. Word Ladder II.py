#IMPORTANT👌💖
#similar to the word ladder part 1
#important question learnt a lot 
#see word ladder solutin first 
#more optimised solution beneath this one 
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

from collections import defaultdict
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        #iniatiallly had only 32 test cases which passes the bfs
        #newly added 3 test cases only passes the bi directional bfs, that too with a lil pruning 
        if endWord not in wordList or beginWord == endWord:
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
        
        front = defaultdict(list)
        back = defaultdict(list)
        
        seen = set()
        
        front[beginWord].append([beginWord])
        back[endWord].append([endWord])
        
        res = []
        flag = True
        
        while front and back and flag:
            # print(front,back)
            tempfront = defaultdict(list)
            tempback = defaultdict(list)
            temp = set()
            
            for u in front:
                lsts = front[u]
                
                if u in seen:
                    continue
                    
                temp.add(u)
                
                for pat in pattern[u]:
                    for v in adj[pat]:
                        if v not in seen and v != u:
                            if v in back:
                                flag = False
                                for lst in lsts:
                                    for lstback in back[v]:
                                        res.append(lst + lstback)
                            else:
                                for lst in lsts:
                                    tempfront[v].append((lst+[v]))
            
            # print(tempfront,flag)
                                
            front = tempfront
            
            if not flag:
                break
                
            for u in back:
                lsts = back[u]
                
                if u in seen:
                    continue
                    
                temp.add(u)
                
                for pat in pattern[u]:
                    for v in adj[pat]:
                        if v not in seen and v!=u:
                            if v in front:
                                flag = False
                                for lst in lsts:
                                    for lstfront in front[v]:
                                        res.append(lstfront + lst)
                            else:
                                for lst in lsts:
                                    tempback[v].append(([v] + lst))
                                    
            # print(tempback,flag)
            
            back = tempback
            seen.update(temp)
        return res
    