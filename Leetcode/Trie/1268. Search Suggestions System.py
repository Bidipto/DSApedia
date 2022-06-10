from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.kids = {}
        self.lst = defaultdict(list)
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        self.root = TrieNode()
        for word in products:
            self.insert(word)
        res = []
        node = self.root
        for i in searchWord:
            if i in node.kids:
                if len(node.lst[i])<=3:
                    res.append(node.lst[i])
                else:
                    res.append(node.lst[i][:3])
                node = node.kids[i]    
            else:
                node.kids = {}
                res.append([])
    
        return res
    def insert(self, word):
        node = self.root
        for i in word:
            if i not in node.kids:
                node.kids[i] = TrieNode()
            node.lst[i].append(word)
            node.lst[i].sort()
            node = node.kids[i]