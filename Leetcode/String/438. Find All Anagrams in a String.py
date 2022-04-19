# 438. Find All Anagrams in a String
from collections import Counter 
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        P = Counter(p)
        S = Counter(s[:len(p)])
        if P == S:
            res = [0]
        else:
            res = []
        for i in range(len(p), len(s)):
            ele = s[i]
            S[ele] += 1
            first = i -len(p)
            S[s[first]] -= 1
            if S == P:
                res.append(first + 1)
        return res
    