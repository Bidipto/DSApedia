# Recover Binary Search Tree
# Recover Binary Search Tree
# DFS solution
def recoverTree(self, root: Optional[TreeNode]):
    self.first = None
    self.second = None
    self.prev = TreeNode(-math.inf)
    def magic(root):
        if not root: return root
        
        magic(root.left)
        
        #if there is not a first node assigned and 
        #the prev node is more than the current node we assign 
        #previous node to the current node
        if not self.first and self.prev.val>root.val:
            self.first = self.prev
        
        #here we keep on storing nodes which are less then first,
        #the last elemnet less than first.val will be our second element
        if self.first and root.val<self.first.val:
            self.second = root
        
        self.prev = root 
        
        magic(root.right)
        
    magic(root)
    self.first.val, self.second.val = self.second.val, self.first.val
# BFS solution
def recoverTree(self, root: Optional[TreeNode]):
    first = None
    second = None
    prev = TreeNode()
    prev.val = -math.inf
    stack = deque([root])
    curr = root.left
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
            
        node= stack.pop()
        

        if not first and prev.val > node.val:
            first = prev
            
        if first and node.val<first.val:
            second = node
            
        prev = node
        
        curr = node.right
    
    
    first.val, second.val = second.val, first.val
        