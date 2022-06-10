from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.kids = defaultdict(TrieNode)
        self.end = False
#step1: Trie banao
#step2: dfs se har subtree ka ek dict banao 
#step3: jis jis subtree ka frequency more then once delete karo
#step4: dfs karke sab path nikalo aur return karo 
class Solution:
    def __init__(self):
        self.root = TrieNode()
        self.dic = defaultdict(list)
        self.res = []
        
    def Trie(self, paths):
        #sorting is reqd cauze later when we make the dict and comapre the subtrees using 
        #the key of the subtree if aint sorted it will give different answers
        for path in sorted(paths):
            node = self.root
            for folder in path:
                node = node.kids[folder] 
                
    def dfs(self, node):
        key = "("
        for i in node.kids:
            key += i+self.dfs(node.kids[i])
        key += ")"
        if key != "()":
            self.dic[key].append(node)      
        return key
    
    def magic(self, node, path):
        if node.end:
            return
        
        for i in node.kids:
            
            self.magic(node.kids[i],path + [i])
            
        if path:
            self.res.append(path)
            
            
        
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        #S1: making the trie 
        #deafult dict used with default value of a TrieNode
        #making life easier
        self.Trie(paths)
        #S2: making a dict of subtrees
        self.dfs(self.root)
        #S3: deleting the subtress with repetations
        for i in self.dic:
            nodelst = self.dic[i]
            if len(nodelst)>1:
                for n in nodelst:
                    n.end = True
        #S4: dfs inf the trie from return values
        self.magic(self.root, [])
        return self.res