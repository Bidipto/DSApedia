#interweaved the old and new linked list 
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        dummy = Node
        #make another linked list 
        curr = head
        
        while curr:
            newNode = Node(curr.val)
            
            nxt = curr.next
            curr.next = newNode
            newNode.next = nxt
            
            curr = curr.next.next
        
        curr = head
        
        while curr:
            nxt = curr.next
            rand = curr.random
            
            if rand != None:
                nextRand = rand.next
                nxt.random = nextRand
            
            curr = curr.next.next
            
        dummy.next = head.next
        prev = dummy
        curr = head
        
        while curr:
            copy = curr.next
            nxt = curr.next.next
            
            prev.next = copy
            prev = prev.next
            
            curr.next = nxt
            curr = curr.next
            
        return dummy.next