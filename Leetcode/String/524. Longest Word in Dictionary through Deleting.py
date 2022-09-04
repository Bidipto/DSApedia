# 524. Longest Word in Dictionary through Deleting

def findLongestWord(self, s: str, words: List[str]) -> str:
    def check(word):
        j = 0
        for i in range(len(s)):
            if s[i] == word[j]:
                j += 1
            if j == len(word):
                return True
        return False
    res = ""    

    #we check for every words in the words list if it matches with the string s, 
    # and store the longest string that mathches
    
    for word in words:
        if len(word)<len(res):
            continue
        
        if check(word):
            if len(word) == len(res):
                if word<res:
                    res = word
            else:
                res = word 
    return res  