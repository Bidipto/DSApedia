# 1160. Find Words That Can Be Formed by Characters
from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = Counter(chars)
        res = 0
        for word in words:
            #my nebber ending love for counter 
            if not Counter(word) - count:
                res += len(word)
        
        return res