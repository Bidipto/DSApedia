# 865. Smallest Subtree with all the Deepest Nodes
def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
#         if root == null,
#         return pair(0, null)

#         if left depth == right depth,
#         deepest nodes both in the left and right subtree,
#         return pair (left.depth + 1, root)

#         if left depth > right depth,
#         deepest nodes only in the left subtree,
#         return pair (left.depth + 1, left subtree)

#         if left depth < right depth,
#         deepest nodes only in the right subtree,
#         return pair (right.depth + 1, right subtree)

        #the intuition is to traverse bottom-up 
        #that happends only in post order traversal 
        #let the node at the deepest levels be at level 1 and root at max level 
        #therefore if the level of the right subtree is equal to the right subtree 
        #we know they are at equal level
        #ps we return a root only when the depth of the right subtree is equal to right
        #and in case id dissimilar depths we supply the root passed 
        #in from the longer subtree
        # [level,root(if any)]
        
        #O(n),O(h)
        def magic(root):
            if not root:
                return [0,None]
            
            left = magic(root.left)
            right = magic(root.right)
            
            #when the depth of left is higher 
            if left[0]>right[0]:
                return [left[0]+1,left[1]]
            elif left[0]<right[0]:
                return [right[0]+1,right[1]]
            else:
                return [left[0]+ 1, root]
        return magic(root)[1]