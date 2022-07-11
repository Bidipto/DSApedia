def isValidSerialization(self, preorder: str) -> bool:
        preorder.split(',')
        slot = 1
        #every node in a binary tree creates two slots, and eats up a slot 
        #if then node is null it doesnt create any slot 
        for i in preorder.split(','):
            # print(i,slot)
            if slot == 0:
                return False
            slot -= 1
            if i != '#':
                slot += 2
        return slot==0