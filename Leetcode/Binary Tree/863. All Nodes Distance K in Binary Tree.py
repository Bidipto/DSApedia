def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
    res = []
    
    def magic(node):
        if not node:
            return -1
        # print(node==target)
        if node == target:
            moreMagic(node,0)
            return 1
        else:
            #if target doesnt lie in a subtree it will return -1
            #else it will return its distance from the node 
            left = magic(node.left)
            right = magic(node.right)
            #if target lies in left 
            if left != -1 and left<=K:
                if left == K: res.append(node.val)
                else: moreMagic(node.right,left+1)
                return left + 1
            elif right != -1 and right<=K:
                if right == K: res.append(node.val)
                else: moreMagic(node.left,right+1)
                return right + 1
            else:
                return -1
            
    def moreMagic(node,dist):
        # print(node.val,dist)
        if not node: return 
        elif dist == K: 
            res.append(node.val)
        else: 
            moreMagic(node.right,dist+1)
            moreMagic(node.left,dist+1)
    
    magic(root)
    return res