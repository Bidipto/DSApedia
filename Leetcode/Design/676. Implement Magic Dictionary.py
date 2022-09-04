# 676. Implement Magic Dictionary
# a hint of word ladder problem
class MagicDictionary:

    def __init__(self):
        self.dic = collections.defaultdict(set)

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            for i in range(len(word)):
                temp = word[:i] + "#" + word[i+1:]
                self.dic[temp].add(word[i])
        # print(self.dic)
    def search(self, word: str) -> bool:
        for i in range(len(word)):
            temp = word[:i] + "#" + word[i+1:]
            # print(temp)
            if temp in self.dic:
                if len(self.dic[temp])>1: 
                    return True
                elif word[i] not in self.dic[temp]:
                    return True
        return False 
