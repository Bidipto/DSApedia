# 429. N-ary Tree Level Order Traversal

from collections import deque

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        que = deque([root])
        res = []
        while que:
            tempres = []
            for i in range(len(que)):
                temp = que.popleft()
                tempres.append(temp.val)
                
                for child in temp.children:
                    que.append(child)
            # print(que)
            res.append(list(tempres))
        return res