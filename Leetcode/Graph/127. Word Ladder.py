from collections import defaultdict,deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #if the endword is not in the list we cant reach it
        if endWord not in wordList:
            return 0
        #if the begin word is not in the list we add it
        if beginWOrd not in wordList:
            wordList.append(beginWord)
        #pattern stores all the wildcards of the word ie cat->[#at,c#t,ca#"]
        pattern = defaultdict(list)
        #adj stores all possible words that can be formed from a wildcard
        #ie c#t->[cat,cut]
        adj = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern[word].append(word[:i] + '#' + word[i+1:])
                adj[word[:i] + '#' + word[i+1:]].append(word)
        # print(pattern,adj)       
        seen = set()
        que = deque([beginWord])
        level = 1
        #now just a simplre bfs for the length of the shorted path 
        while que:
            level += 1
            # print(que)
            for q in range(len(que)):
                u = que.popleft()
                
                if u in seen:
                    continue
                seen.add(u)
                
                for pat in pattern[u]:
                    for v in adj[pat]:
                        # print(u,v,)
                        if v not in seen:
                            if v == endWord:
                                return level
                            que.append(v)
        return 0             