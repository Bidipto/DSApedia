# 916. Word Subsets

def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
    s = set()
    res = []
    test = collections.Counter()
    
    #calculated the union counter of all words in the words2 
    
    for i,word in enumerate(words2):
        c = collections.Counter(word)
        temp = c - test
        test += temp 
        
    # print(test)
    
    for word in words1:
        count = collections.Counter(word)
        if not test-count:
            res.append(word)
            
    return res