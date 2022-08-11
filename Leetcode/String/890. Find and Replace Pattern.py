# 890. Find and Replace Pattern

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        test = self.magic(pattern)
        # print(test)
        res = []
        for word in words:
            temp = self.magic(word)
            # print(temp)
            if temp == test:
                res.append(word)
        return res
    
    def magic(self,word):
        dic = {}
        
        code = 1
        codeCount = 1
        
        dic[word[0]] = code
        pre = word[0]
        count = 0
        
        res = []
        
        for i in word:
            if i == pre:
                count += 1 
            else:
                res.append((count,code))
                if i in dic:
                    code = dic[i]
                else:
                    code = codeCount + 1
                    codeCount += 1
                    dic[i] = code 
                count = 1 
                pre = i
        res.append((count,code))
        return res