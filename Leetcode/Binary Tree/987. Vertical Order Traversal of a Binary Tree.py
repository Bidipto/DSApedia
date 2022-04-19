# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
from collections import deque
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = defaultdict(list)
        que = deque([(root,0)])
        res[0].append(root.val)
        while que:
            #temp dic to store the nodes level at a particular horis=zontal level
            #since if there are multiple nodes at the same level we need to apppend them
            #in a sorted way 
            dic = defaultdict(list)
            for i in range(len(que)):
                node,level = que.popleft()
                if node.left:
                    dic[level-1].append(node.left.val)
                    que.append([node.left,level-1])
                    
                if node.right:
                    dic[level+1].append(node.right.val)
                    que.append([node.right,level+1])
            for i in dic:
                res[i].extend(sorted(dic[i]))

        ans = []
        
        #appending the the nodes at every level sequentially
        for i in sorted(res.keys()):
            ans.append(res[i])
            
        return ans