class TrieNode:
    def __init__(self):
        self.kids = {}
        self.end = -1

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, I):
        node = self.root
        node.end = I
        for i in word:
            if i not in node.kids:
                node.kids[i] = TrieNode()
            node = node.kids[i]
            node.end = I
        
    def search(self, word):
        node = self.root
        for i in word:
            if i not in node.kids:
                return -1
            node = node.kids[i]
        return node.end

class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for i,word in enumerate(words):
            for j in range(len(word)):
                # print(word[j:] + '#' + word[::-1],i)
                self.trie.insert(word[j:] + '#' + word,i)
        
    def f(self, prefix: str, suffix: str) -> int:
        # print(suffix + "#" + prefix)
        return self.trie.search(suffix + "#" + prefix)

