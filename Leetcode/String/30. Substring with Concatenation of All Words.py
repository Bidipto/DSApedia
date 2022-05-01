# 30. Substring with Concatenation of All Words
from collections import defaultdict
from collections import Counter
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        def magic(start):
            temp = Counter()
            for i in range(0,LenOfSubstr-LenOfWord+1,LenOfWord):
                temp[s[start+i:start+i+LenOfWord]] += 1
            
            # print(start, temp)
            if temp == worddic:
                res.append(start)
            #i = 0,3,6,9 for start = 0
                #i = 3 lenword = 6
                #end = 9 #9-3 = 6
            #i = 1,4,7,10 for start = 1
            for i in range(start+LenOfWord, LenOfString - LenOfWord + 1, LenOfWord):
                temp[s[i-LenOfWord:i]] -= 1
                # print(s[i+LenOfSubstr-LenOfWord:i+LenOfSubstr])
                temp[s[i+LenOfSubstr-LenOfWord:i+LenOfSubstr]] += 1
                if temp == worddic:
                    res.append(i)
         #main idea is we make a counter of the given words to match
        #and then compute the counter of the same lengths of the string one by one
        res = []    
            
        worddic = Counter(words)
            
        LenOfWord = len(words[0])
        LenOfString = len(s)
        LenOfSubstr = LenOfWord * len(words)
        # print(LenOfSubstr,LenOfWord)
        for start in range(min(LenOfWord, LenOfString - LenOfSubstr + 1)):
            #function call for each start value
            magic(start)
            
        return res