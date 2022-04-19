# Kth Smallest Element in a BST
#modified inorder traversal could be done using bfs also
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = k
        self.res = None
        def magic(root):
            if not root: return
            
            magic(root.left)
            
            self.count -= 1
            if self.count == 0:
                self.res = root.val
                return
            magic(root.right)
            
        magic(root)
        return self.res