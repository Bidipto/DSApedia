# 86. Partition List

def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
    dummy = ListNode(-1)
    dummy.next = head 
    
    end = dummy
    
    pre = dummy
    curr = head 
    
    while curr:
        if curr.val<x:
            if end == pre:
                #if there is not element greater or equal to k
                end = end.next
                curr = curr.next
                pre = pre.next
            else:
                #removing the node
                nxt = curr.next
                pre.next = nxt

                curr.next = None 

                #joining the node after end(last node )
                temp = end.next
                end.next = curr
                curr.next = temp
                end = curr

                curr = nxt
        else:
            curr = curr.next
            pre = pre.next
    return dummy.next