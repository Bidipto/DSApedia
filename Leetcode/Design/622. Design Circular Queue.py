class Node:
    def __init__(self,val=-1,prev=None,nxt=None):
        self.val = val
        self.prev = prev
        self.next = nxt

# from collections import deque
class MyCircularQueue:

    def __init__(self, k: int):
        self.size = 0
        self.N = k
        self.back = None
        self.front = None
        # self.de = deque()
        

    def enQueue(self, value: int) -> bool:
        if not self.size:
            # self.de.append(value)
            temp = Node(value)
            self.front = temp
            self.back = temp 
            self.size += 1
            return True
        elif self.size<self.N:
            # self.de.append(value)
            temp = Node(value,self.front,None)
            self.front.next = temp
            self.front = temp
            self.size += 1
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if not self.size:
            return False
        elif self.size == 1:
            # self.de.popleft()
            self.back = None
            self.front = None
            self.size -= 1
        else:
            # print(self.size,self.front.val,self.back.val)
            # self.de.popleft()
            temp = self.back.next
            temp.prev = None
            self.back = temp 
            self.size -= 1
        return True

    def Front(self) -> int:
        # print(deque)
        if self.size:
            return self.back.val
        return -1

    def Rear(self) -> int:
        # print(deque)
        if self.size:
            return self.front.val
        return -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.N
