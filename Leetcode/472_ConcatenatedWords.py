# 472. Concatenated Words
# TLE approach
from collections import Counter
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wordset = set()
        res = []
        words.sort(key=len)
        #The idea is to sort the words according to the len
        #and the while iterating thru the sorted words list 
        #the current word would be the string and all previous words would be the worddict
        #the constrains are a bit tought
        
        for word in words:
            if self.wordbreak(word,wordset):
                res.append(word)
            wordset.add(word)
            
        return res
    
    def wordbreak(self, word, wordset):
        if not wordset:
            return False
        dp = [False]*(len(word)+1)
        dp[-1] = True
        
        for i in range(len(word)-1,-1,-1):
            for w in wordset:
                if i + len(w)<=len(word) and word[i:i+len(w)] == w and dp[i+len(w)]:
                    dp[i] = 1
                    break
        return dp[0]

#my AC solution 
#tbh loved solving this
def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        dp = {}
        words = set(words)
        res = []
        
        def dfs(word):
            if word in dp.keys():
                return dp[word]
            
            dp[word]=False
            
            #i qki minmimun mumber of words should be 2
            for i in range(1,len(word)):
                prefix = word[:i]
                suffix = word[i:]
                
                if prefix in words:
                    if suffix in words:
                        dp[word] = True 
                        break
                    elif dfs(suffix):
                        dp[word] = True
                        break
            return dp[word]

        for word in words:
            if dfs(word):
                res.append(word) 

        return res

#also a similar version in GFG where we are to return the number of possible ways to concatenate the numbers
#in only pairs of i,j and i and j should belong in the numberdict supplied
#only trick is to deal with duplicates in the numberdict 
#counter comes handy here
def countPairs(self, N, word, numbers): 
        res = 0
        words = [str(i) for i in numbers]
        counter = Counter(words)
        word = str(word)
        words = set(words)
    
        #i qki minmimun mumber of words should be 2
        for i in range(1,len(word)):
            prefix = word[:i]
            suffix = word[i:]
            
            if prefix in words:
                if suffix == prefix:
                    res += counter[suffix]*(counter[suffix]-1)
                elif suffix in words:
                    res += counter[prefix] * counter[suffix] 
            
        return res
            