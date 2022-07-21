# 590. N-ary Tree Postorder Traversal

def postorder(self, root: 'Node') -> List[int]:
        res = []
        
        def magic(root):
            if not root: return 
            
            for child in root.children:
                magic(child)
                
            res.append(root.val)   
            
        magic(root)
        return res