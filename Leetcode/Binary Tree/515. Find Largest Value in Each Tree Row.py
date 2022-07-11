#learn to use lambda ASAP
from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        d = defaultdict(lambda : -math.inf)
        
        def magic(node,level):
            if not node:
                return 

            d[level] = max(d[level], node.val)

            magic(node.left,level+1)
            magic(node.right,level+1)
            
        magic(root,0)
        res = []

        for i in sorted(d):
            res.append(d[i])
        return res