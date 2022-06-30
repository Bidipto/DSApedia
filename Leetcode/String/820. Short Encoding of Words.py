# 820. Short Encoding of Words

# eleminating word that could come inside a word in the dictionary
def minimumLengthEncoding(self, words: List[str]) -> int:
    s = set(words)
    for word in words:
        for i in range(1,len(word)):
            if word[i:] in s:
                s.discard(word[i:])
    
    return sum(len(word)+1 for word in s)