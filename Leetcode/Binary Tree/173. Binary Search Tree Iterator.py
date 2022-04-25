#O(h) space solution with inorder bfs
#the the fact the stack in inorder traversal has the least element at the top is used for this solution
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.update(root)
            
    def update(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        res = self.stack.pop()
        self.update(res.right)
        return res.val

    def hasNext(self) -> bool:
        return not len(self.stack) == 0

#O(n) naive solution
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.res = []
        def magic(root):
            if not root: return 
            magic(root.left)
            self.res.append(root.val)
            magic(root.right)
            
        magic(root)
        print(self.res)
        self.i = -1
        self.len = len(self.res)

    def next(self) -> int:
        self.i += 1
        return self.res[self.i]

    def hasNext(self) -> bool:
        return self.i+1<self.len