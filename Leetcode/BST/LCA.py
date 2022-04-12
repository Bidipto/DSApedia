def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    #ensuring that q is always smaller
    if q.val<p.val:
        p,q = q,p
    #recursive function for LCA
    def magic(node):
        if not node: return
        #if one of the nodes is the current node therefore curnode will be LCA
        elif node == p or node == q:
            return node
        #the first time when the p and q lie on either side of a node its
        #the LCA of the node
        elif p.val<node.val<q.val:
            return node
        #if both p and q are smaller or greater we move to left or right
        elif p.val<q.val<node.val:
            return magic(node.left)
        else:
            return magic(node.right)
        
    return magic(root)