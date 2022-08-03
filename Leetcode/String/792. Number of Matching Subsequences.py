def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        #map ke saath optimizations 
        res = 0
        N = len(words)
        index = collections.defaultdict(list)
        
        for word in words:
            index[word[0]].append(word)
        
        for i in s:
            if not index[i]:
                continue
            temp = index[i].copy()
            index[i] = []
            for w in temp:
                if w == i:
                    res += 1
                else:
                    index[w[1]].append(w[1:])
            
            
        return res