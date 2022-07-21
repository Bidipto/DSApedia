class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        
        def magic(root):
            if not root: return 
            
            res.append(root.val)
            
            for child in root.children:
                magic(child)
                
        magic(root)
        
        return res