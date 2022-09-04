# Given a Binary Tree (BT), convert it to a Doubly Linked List(DLL) In-Place. 
# The left and right pointers in nodes are to be used as previous and next pointers respectively in converted DLL. 
# The order of nodes in DLL must be same as Inorder of the given Binary Tree. 
# The first node of Inorder traversal (leftmost node in BT) must be the head node of the DLL.

class Solution:
    def bToDLL(self,root):
        self.prev = None 
        self.head = None 
        def magic(root):
            if not root:
                return None 
            
            magic(root.left )
            
            if not self.prev:
                self.prev = root 
                self.head = root 
            else:
                self.prev.right = root
                root.left = self.prev 
                self.prev = root 
                
            magic(root.right)
            
        magic(root)
        
        return self.head