class Node:
    def __init__(self,val=-1,prev=None,nxt=None):
        self.val = val
        self.prev = prev
        self.next = nxt


class MyCircularDeque:

    def __init__(self, k: int):
        self.size = 0
        self.N = k
        self.back = None
        self.front = None
        

    def insertFront(self, value: int) -> bool:
        if not self.size:
            temp = Node(value)
            self.front = temp
            self.back = temp 
            self.size += 1
            return True
        elif self.size<self.N:
            temp = Node(value,self.front,None)
            self.front.next = temp
            self.front = temp
            self.size += 1
            return True
        else:
            return False 
        

    def insertLast(self, value: int) -> bool:
        if not self.size:
            temp = Node(value)
            self.front = temp
            self.back = temp 
            self.size += 1
            return True
        elif self.size<self.N:
            temp = Node(value,None,self.back)
            self.back.prev = temp
            self.back = temp
            self.size += 1
            return True
        else:
            return False 
        

    def deleteFront(self) -> bool:
        if not self.size:
            return False
        elif self.size == 1:
            self.back = None
            self.front = None
            self.size -= 1
        else:
            temp = self.front.prev
            temp.next = None
            self.front = temp 
            self.size -= 1
        return True
        

    def deleteLast(self) -> bool:
        if not self.size:
            return False
        elif self.size == 1:
            self.back = None
            self.front = None
            self.size -= 1
        else:
            # print(self.size,self.front.val,self.back.val)
            temp = self.back.next
            temp.prev = None
            self.back = temp 
            self.size -= 1
        return True
        

    def getFront(self) -> int:
        if self.size:
            return self.front.val
        else:
            return -1
        

    def getRear(self) -> int:
        if self.size:
            return self.back.val
        else:
            return -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.N
