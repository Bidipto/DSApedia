class stack:
    def __init__(self,val,minn,nxtNode):
        self.val = val
        self.minn = minn
        self.next = nxtNode
class MinStack:

    def __init__(self):
        self.head = None

    def push(self, val: int) -> None:
        if self.head == None:
            self.head = stack(val,val,None)
        else:
            self.head = stack(val,min(self.head.minn,val),self.head)
    def pop(self) -> None:
        self.head = self.head.next

    def top(self) -> int:
        return self.head.val

    def getMin(self) -> int:
        return self.head.minn