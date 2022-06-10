from collections import deque
class TrieNode:
    def __init__(self):
        self.kids = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for i in word:
            if i not in node.kids:
                node.kids[i] = TrieNode()
            node = node.kids[i]
        node.end = True

    def search(self, word: str) -> bool:
        n = self.root
        stack = deque([n])
        for i in word:
            for j in range(len(stack)):
                node = stack.popleft()
                if i == ".":
                    for kid in node.kids:
                        stack.append(node.kids[kid])
                elif i in node.kids:
                    stack.append(node.kids[i])
            if not stack: return False
        for node in stack:
            if node.end: return True
        return False