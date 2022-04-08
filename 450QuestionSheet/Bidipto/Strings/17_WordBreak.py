#staring from end we see that can we reach the end, if we reach the end we store a 0
#similarly we do for all the letters 

def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    dp = [-1] * (len(s) + 1)
    dp[len(s)] = 0
    for i in range(len(s), -1, -1):
        for word in wordDict:
            #print(s[i:i + len(word)],i,word,dp)
            if i + len(word) <= len(s) and s[i: i + len(word)] == word:
                if dp[i + len(word)] == 0:
                    dp[i] = 0
                    break
    return True if dp[0] == 0 else False