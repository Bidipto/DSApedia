#recursive solution
#     Recursively call function increasingBST(TreeNode root, TreeNode tail)
# tail is its next node in inorder,
# （the word next may be easier to understand, but it’s a keyword in python)

# If root == null, the head will be tail, so we return tail directly.

# we recursively call increasingBST(root.left, root),
# change left subtree into the linked list + current node.

# we recursively call increasingBST(root.right, tail),
# change right subtree into the linked list + tail.

# Now the result will be in a format of linked list, with right child is next node.
# Since it's single linked list, so we set root.left = null.
# Otherwise it will be TLE for Leetcode judgment to traverse over your tree.

# The result now is increasingBST(root.left) + root + increasingBST(root.right).

# One tip here, we should arrange the old tree, not create a new tree.
# The leetcode judgment comparer only the values,
# so it won't take it as wrong answer if you return a new tree,
# but it is wrong.
def increasingBST(self, root: TreeNode, tail = None) -> TreeNode:
    if not root: return tail
    res = self.increasingBST(root.left,root)
    root.left = None
    root .right = self.increasingBST(root.right,tail)
    
    return res

#iterative solution
#basic iterative inorder with some modifications
def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root: return 
        stack = []
        current = previous = root
        flag = True
         
        while stack or current:
            
            while current:
                stack.append(current)
                current = current.left
                
            node = stack.pop()
            
            if flag:
                newNode = node
                previous = node
                flag = not flag
            else:
                previous.right = node
                previous.left = None
                previous = previous.right
            
            # print(previous.val,previous.right.val,previous.left.val)
            current = node.right
        previous.right = None
        previous.left = None
            
        return newNode
#some more optimization on the iterative soln
#we can use a dummy node and stay away from using flags