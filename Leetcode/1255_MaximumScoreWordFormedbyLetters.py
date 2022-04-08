# 1255. Maximum Score Words Formed by Letters HARD 
from collections import Counter
#Counter is more powerful than i think lol
#kafi next level question actually just requires a bit of thinking 
#otherwise good to go
#this can be converted to a dp solution with a 1D [] where i would represent the max we can 
#make at that index
#but the remaining letters would be also different 
#something need to think about
class Solution:
    def maxScoreWords(self, word: List[str], letters: List[str], score: List[int]) -> int:
        scores = [sum(score[ord(c)-ord("a")] for c in w) for w in word]
        words = [Counter(w) for w in word]
        # print(Counter(letters))
        # print(scores)
        
        res = [0]
        
        def magic(i,currscore,rem):
            res[0] = max(res[0],currscore)
            
            for j,counterwords in enumerate(words[i:],i):
                if not counterwords - rem:
                    # print(i,j,currscore + scores[j],rem-counterwords)
                    magic(j+1,currscore + scores[j],rem-counterwords)
        
        magic(0,0,Counter(letters))
        return res[0]