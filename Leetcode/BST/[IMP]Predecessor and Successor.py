# https://practice.geeksforgeeks.org/problems/predecessor-and-successor/1

# we perform binary search on the bst to find the predecessor and successor of the key
# kafi good question 
# got thinky and overcomplicated it 
# looks like i have to solve the striver sheet ASAP

def findPreSuc(root, pre, suc, key):
    temp = root
    while temp:
        if temp.key > key:
            suc[0] = temp
            temp = temp.left
        else:
            temp = temp.right
    
    temp = root
    while temp:
        if temp.key < key:
            pre[0] = temp
            temp = temp.right
        else:
            temp = temp.left
 