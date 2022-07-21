# 61. Rotate List

def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return head 
        
        count = 1
        fast = head
        
        while fast.next:
            count += 1
            fast = fast.next 
            
        k %= count
        
        if k == 0: return head
            
        end = head
        for i in range(count-k-1):
            end = end.next
            
        newHead = end.next 
        fast.next = head 
        end.next = None
        
        return newHead 