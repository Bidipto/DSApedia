# 968. Binary Tree Cameras

#for every level we maintain 3 states, one where it has a camera, two when when its covered and third when its not 
#for being not covered we should have the left and right node covered
#for being covered we have two option 
#1. we can have a camera in the left and right node must be covered
#2. we can have a camera in the right and left node must be covered
#for haveing a camera we actually dont care what state the left and right nodes are in 
def minCameraCover(self, root: Optional[TreeNode]) -> int:
    def magic(root):
        if not root:
            return [0,0,math.inf]
        
        left = magic(root.left)
        right = magic(root.right)
        
        
        notCovered = left[1]+right[1]
        covered = min(right[2] + min(left[1:]),left[2] + min(right[1:]))
        camera = min(left) + min(right) + 1
        
        return [notCovered, covered, camera]
    
    res = magic(root)
    return (min(res[1:]))