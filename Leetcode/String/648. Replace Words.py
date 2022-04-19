# 648. Replace Words
def replaceWords(self, dictionary: List[str], sentence: str) -> str:
    arr = list(sentence.split(' '))
    lenn = set()
    for i in dictionary:
        lenn.add(len(i))
    lenn = list(lenn)
    lenn.sort()
        
    dic = set(dictionary)
    
    for i in range(len(arr)):
        word = arr[i]
        for j in lenn:
            if j <= len(word):
                if word[:j] in dic:
                    arr[i] = word[:j]
                    break    
            else:
                break
                
    return " ".join(arr)