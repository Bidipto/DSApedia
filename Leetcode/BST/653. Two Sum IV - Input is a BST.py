# 653. Two Sum IV - Input is a BST
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        #learnt generator
        #generator vs iterator 
        #second impletation is based on the bst iterator concept 
        def first(root):
            if root:
                yield from first(root.left)
                yield root
                yield from first(root.right)
            
        def last(root):
            if root:
                yield from last(root.right)
                yield root
                yield from last(root.left)
        
        firstgen = first(root)
        lastgen = last(root)
        lo = next(firstgen)
        hi = next(lastgen)
        
        while lo.val < hi.val:
            # print(lo.val,hi.val)
            if lo.val + hi.val == k:
                return True
            elif lo.val + hi.val>k:
                hi = next(lastgen)
            else:
                lo = next(firstgen)
                
        return False