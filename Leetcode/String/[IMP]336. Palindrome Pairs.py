# 336. Palindrome Pairs

def palindromePairs(self, words: List[str]) -> List[List[int]]:
    #if the prefix of the word is a palindrome then if we add the reversed suffix of the word,
    #it becomes a plaindrome
    # acaba where aca is a palindrome is ba is the sufix
    # if we add ab to the word it becomes a palindrome 

    #first we will make a dict with key as the word and value as its pair
    res = []

    dic = {word:i for i,word in enumerate(words)}
    #print(dic)

    for word,i in dic.items():
        # print(word, i)
        N = len(word)
        for j in range(N+1):
            prefix = word[:j]
            suffix = word[j:]

            if self.check(prefix):
                search = suffix[::-1]
                #to prevent dublicates 
                if search != word and search in dic:
                    #print(word, prefix, search,[dic[search], i])
                    res.append([dic[search], i])

            if j != N and self.check(suffix):
                search = prefix[::-1]
                #to prevent dublicates 
                if search != word and search in dic:
                    #print(word, suffix, search, [i, dic[search]] )
                    res.append([i, dic[search]])

    return res
            
def check(self, word):
    return word == word[::-1]