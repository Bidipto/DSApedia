# 101. Symmetric Tree
def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        #loook up for the recursive apporoach
        que = deque()
        lst = list()
        que.append(root)
        while que:
            for i in range(len(que)):
                node = que.popleft()
                
                if node.left:
                    que.append(node.left)
                    lst.append(node.left.val)
                else:
                    lst.append(101)
                if node.right:
                    que.append(node.right)
                    lst.append(node.right.val)
                else:
                    lst.append(101)
            # print(lst,lst.reverse())       
            if lst != lst[::-1]:
                return False
            lst = list()
            
        return True