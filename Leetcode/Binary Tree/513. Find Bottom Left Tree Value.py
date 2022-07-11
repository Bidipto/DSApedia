# 513. Find Bottom Left Tree Value

def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        #simple dfs with track from elements of all levels, bfs se bhi kar hi sakte ha
        d = defaultdict(list)
        
        def magic(node,level):
            if not node:
                return 
            
            d[level].append(node.val)
            
            magic(node.left,level+1)
            magic(node.right,level+1)
            
        magic(root,0)
        
        return d[max(d)][0]