# 328. Odd Even Linked List
# misunderstood the question initially but linked lists are kinda hard to heal with right? maybe 
def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head 
        
        dummy2 = ListNode(-1)
        
        pre = dummy
        curr = head 
        preeven = dummy2   
        flag = True
        
        while curr:
            # print(curr.val)
            if flag:
                pre = pre.next
                curr = curr.next
                flag = False 
                
            else:
                nxt = curr.next 
                pre.next = nxt
                
                preeven.next = curr
                preeven = preeven.next
                
                curr=nxt
                
                flag = True
        preeven.next = None
        pre.next = dummy2.next
        return dummy.next