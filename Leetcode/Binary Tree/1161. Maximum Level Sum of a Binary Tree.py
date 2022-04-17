# 1161. Maximum Level Sum of a Binary Tree
def maxLevelSum(self, root: Optional[TreeNode]) -> int:
    #this approach aslo calculates the sum one step ahead
    #kinda a little dirty
    que= deque([root])
    temp = root.val
    level = 1
    res = 1
    maxx = root.val
    while que:
        temp = 0
        level += 1
        # print(level,que)
        for i in range(len(que)):
            node = que.popleft()
            if node.right:
                que.append(node.right)
                temp += node.right.val
            if node.left:
                que.append(node.left)
                temp += node.left.val
        if temp>maxx and que:
            maxx = temp
            res = level
    return res