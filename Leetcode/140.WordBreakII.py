# 140. Word Break II
from collections import defaultdict
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dp = defaultdict(list)
        #"catsanddog"
        #"0123456789"
        
        #wanted to start from but then realise wont be to return the ans cause the
        #final ans wont be accessable at a single,thora code karke ho jayega 
        #but it better from back ,🤣
        for i in range(len(s)-1,-1,-1):
            for word in wordDict:
                if i + len(word)<=len(s) and s[i:i+len(word)] == word:
                    #two cases one if its the last word or one if its in between
                    #case 1: when its the last word ie i + len(word) == len(s)
                    if i + len(word) == len(s):
                        dp[i].append(word)
                    #case 2: when its in between 
                    #we can check if dp[i + len(word)] exists but then 
                    #defaultdict ka faida uthaya jaye
                    else:
                        for lastword in dp[i+len(word)]:
                            dp[i].append(word + " " + lastword)
        return dp[0]

#memoiization bhi kar hi lena