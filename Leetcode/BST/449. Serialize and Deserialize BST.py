# 449. Serialize and Deserialize BST

#very similar to validate binary search tree

class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.res = []
        def magic(node):
            if not node:
                return 
            
            self.res.append(node.val)
            magic(node.left)
            magic(node.right)
        
        magic(root)
        return ",".join([str(i) for i in self.res])

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data: return None 
        data = data.split(",")
        N = len(data)
        # print(data)
        
        def magic(i,minn,maxx):
            # print(i,minn,maxx)
            if i >= N:
                return None,i-1
            
            val = int(data[i])
            
            if val<minn or val>maxx:
                return None,i-1
            
            node = TreeNode(int(data[i]))
            
            node.left,j = magic(i+1,minn,val)
            node.right,k = magic(j+1,val,maxx)
            
            return node,k
            
        head,i = magic(0,-math.inf,math.inf)
        return head 
        