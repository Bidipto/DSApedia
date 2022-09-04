#loosely based on the reorder list problem

def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head 
        fast = head 
        #middle
        while fast.next and fast.next.next:
            slow = slow.next 
            fast = fast.next.next 
        
        #reverse from middle
        prev = None 
        curr = slow.next
        while curr:
            temp = curr.next 
            curr.next = prev
            
            prev = curr 
            curr = temp 
        
        head2 = prev 
        slow.next = None 
        
        #calculate
        res = -math.inf 
        
        while head:
            res = max(res,(head.val+head2.val))
            head = head.next
            head2 = head2.next
            
        return res
            