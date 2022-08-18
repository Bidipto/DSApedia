#recursive approach but a little bit on the rough side 

def reorderList(self, head: Optional[ListNode]) -> None:
    if not head.next or not head:
        return head 
    
    self.pre = head 
    self.curr = head.next 
    
    def magic(node):
        if node.next:
            magic(node.next)
            
        if not self.curr:
            return 
        
        print(node.val,self.pre.val,self.curr.val)    

        if node == self.curr:
            node.next = None
            self.curr = None 
            return 


        self.pre.next = node
        node.next = self.curr

        self.pre = self.curr
        self.curr = self.curr.next
        
    magic(head)