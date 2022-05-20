# 146. LRU Cache
#a double linked list 
class Node:
    
    def __init__(self, val=None,value=None):
        self.val = val
        self.value = value
        self.left = None
        self.right = None

class LRUCache:

    def __init__(self, capacity: int):
        #dictionary with key as value and the node as the value
        self.dic = {}
        self.capacity = capacity
        self.lru = Node()
        self.recent = Node()
        self.lru.right = self.recent
        self.recent.left = self.lru
        #print(self.lru)
        
    def remove(self, node):
        pre = node.left
        nxt = node.right
        
        pre.right = nxt
        nxt.left = pre
        
    def append(self, node):
        nxt = self.recent
        pre = nxt.left
        
        
        pre.right = node
        nxt.left = node
        
        node.right = nxt
        node.left = pre
    
    def get(self, key: int) -> int:
        #if the key exits we return its value and remove the node
        #bring it to the front 
        if key in self.dic:
            node = self.dic[key]
            self.remove(node)
            self.append(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        #if the key already exits we just modify the value by accesing
        #the node and then move it to the front 
        if key in self.dic:
            node = self.dic[key]
            node.value = value
            self.remove(node)
            self.append(node)
        #if it doesnt exist we just create a new one and put it up front
        else:
            node = Node(key, value)
            self.append(node)
            self.dic[key] = node
            #if the capacity exceeds we remove the lru
            if len(self.dic)>self.capacity:
                lru = self.lru.right
                self.remove(lru)
                del self.dic[lru.val]
