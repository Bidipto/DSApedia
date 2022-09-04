# 720. Longest Word in Dictionary

def longestWord(self, words: List[str]) -> str:
    dic = {word:False for word in words}
    resLen = 0
    res = ""
    # print(dic)
    for word in sorted(words):
        # print(word,res,word[:len(word)-1],dic)
        if len(word) == 1:
            if len(word)>resLen:
                resLen = len(word)
                res = word
            dic[word] = True
        elif word[:len(word)-1] in dic and dic[word[:len(word)-1]] == True:
            dic[word] = True
            if len(word)>resLen:
                resLen = len(word)
                res = word
    return res