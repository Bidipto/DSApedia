# 993. Cousins in Binary Tree
def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
    #did using flags but could be done if er stored the parent value with kid value in pairs
    queue = deque([root])
    res = []
    #root will always be the right most element after the for loop
    while queue:
        a = False
        b = False
        for i in range(len(queue)):
            temp = False
            root = queue.popleft()
            if root.left:
                queue.append(root.left)
                if root.left.val == x:
                    a = not a
                    temp = not temp
                elif root.left.val == y:
                    b = not b
                    temp = not temp
            if root.right:
                queue.append(root.right)
                if root.right.val == x:
                    a = not a
                    if temp: return False
                elif root.right.val == y:
                    b = not b
                    if temp: return False
        if a and b:
            return True
        if a or b:
            return False
        
    return False
    