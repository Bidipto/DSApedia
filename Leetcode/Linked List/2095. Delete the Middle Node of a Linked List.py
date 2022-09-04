# 2095. Delete the Middle Node of a Linked List

def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(-1)
    dummy.next = head 
    prev = dummy 
    
    slow = head 
    fast = head 
    
    while fast and fast.next:
        prev = prev.next 
        slow = slow.next 
        fast = fast.next.next
        
    prev.next = slow.next 
    slow.next = None 
    
    return dummy.next 