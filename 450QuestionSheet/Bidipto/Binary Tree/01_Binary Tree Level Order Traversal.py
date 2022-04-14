# Binary Tree Level Order Traversal
def levelOrder(self, root):
    if not root:
        return []
    
    queue = deque([root])
    res = []
    #root will always be the right most element after the for loop
    while queue:
        temp = []
        for i in range(len(queue)):
            root = queue.popleft()
            if root.left:
                queue.append(root.left)
            if root.right:
                queue.append(root.right)
            temp.append(root.val)
        res.append(temp)
    return(res)
    