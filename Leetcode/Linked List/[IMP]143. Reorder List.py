# 143. Reorder List

#3 step code
def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return 
        #find middle 
        slow = head 
        fast = head 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print(slow.val)
        #reverse after middle 
        prev = None 
        curr = slow.next 
        while curr:
            temp = curr.next
            curr.next = prev 
            
            prev = curr 
            curr = temp 
        head2 = prev 
        slow.next = None 
        #join both
        flag = True 
        while head and head2:
            nxt1 = head.next
            nxt2 = head2.next
            
            head.next = head2
            head2.next = nxt1
            
            head = nxt1
            head2 = nxt2
            
        












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