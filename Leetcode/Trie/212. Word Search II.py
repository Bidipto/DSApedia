#preety hard hard problem
from collections import defaultdict
#build a trie of words
#then perform dfs on all the elements of the matrix 


class TrieNode:
    def __init__(self):
        self.kids = defaultdict(TrieNode)
        self.isword = False
class Solution:
    def __init__(self):
        self.root = TrieNode()
        self.res = []
        
    def Trie(self, words):
        for word in words:
            node = self.root
            for c in word:
                node = node.kids[c]
            node.isword = True
                
    def magic(self, i, j, node, path):
        # all the word to res if we a reaach a word
        # also turn node.isword false qki what if a longer word with this word as prefix
        # for the same reason we should return now
        if node.isword:
            self.res.append(path)
            node.isword = False
        if i<0 or j<0 or i>=self.M or j>=self.N:
            return
        char = self.board[i][j]
        newnode = node.kids.get(char)
        if not newnode:
            return 
        
        self.board[i][j] = '#'
        
        self.magic(i+1, j, newnode, path + char)
        self.magic(i-1, j, newnode, path + char)
        self.magic(i, j+1, newnode, path + char)
        self.magic(i, j-1, newnode, path + char)
        
        self.board[i][j] = char 
        
        
                
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.M = len(board)
        self.N = len(board[0])
        self.board = board
        #building tree
        self.Trie(words)
        #lopping the matrix:
        for i,j in product(range(len(board)), range(len(board[0]))):
            self.magic(i, j, self.root, "")
            
        return self.res
        