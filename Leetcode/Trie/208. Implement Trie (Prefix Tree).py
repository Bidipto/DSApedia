# 208. Implement Trie (Prefix Tree)
class TrieNode:
    def __init__(self):
        self.kids = {}
        self.end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for i in word:
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

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for i in prefix:
            if i not in node.kids:
                return False
            node = node.kids[i]
        return True