class TrieNode:
    def __init__(self):
        self.kids = {}
        self.end = False
        
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for i in word[1:]:
            if node.end:
                break
            if i not in node.kids:
                node.kids[i] = TrieNode()
            node = node.kids[i]
        node.end = True
        
    def search(self, word: str) -> bool:
        node = self.root
        for i in word:
            if i not in node.kids:
                return False
            node = node.kids[i]
        return node.end

class Solution:
    def __init__(self):
        self.root = TrieNode()
        
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        for w in folder:
            self.insert(w.split('/'))
        
        res = []
        def magic(node,path):
            if node.end:
                res.append(path)
                return
                
            for kid in node.kids:
                magic(node.kids[kid],path + '/' + kid)
    
        magic(self.root,"")
        return res
    
    
    
    def insert(self, word: str) -> None:
        node = self.root
        for i in word[1:]:
            if node.end:
                break
            if i not in node.kids:
                node.kids[i] = TrieNode()
            node = node.kids[i]
        node.end = True