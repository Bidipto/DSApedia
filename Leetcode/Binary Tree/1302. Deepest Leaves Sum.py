#we have to return the last sum of the last level of the binary tree
#basically dfs upto to the last level
from collections import deque
def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
    que= deque([root])
    temp = root.val
    while que:
        res
        res = temp
        temp = 0
        for i in range(len(que)):
            node = que.popleft()
            if node.right:
                que.append(node.right)
                temp += node.right.val
            if node.left:
                que.append(node.left)
                temp += node.left.val
    return res

 #slightly different from the above on how i am storing the level sum 
 #instead of calculating the sum of the new queue formed after an iteration i am calculating
 #the sum of the nodes being popped from the queue
 #basically more adaptable to the problem related to levels
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        que= deque([root])
        while que:
            res = 0
            for i in range(len(que)):
                node = que.popleft()
                res += node.val
                if node.right:
                    que.append(node.right)
                if node.left:
                    que.append(node.left)
        return res