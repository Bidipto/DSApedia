# 2181. Merge Nodes in Between Zeros
# we can optimize in-place using constant space as well

def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        summ = 0
        res = []
        while head:
            if head.val == 0:
                res.append(0)
            else:
                res[-1] += head.val
                
            head = head.next
        
        res.pop()
        dummy = ListNode(0)
        curr = dummy
        
        for i in res:
            temp = ListNode(i)
            curr.next = temp
            curr = temp
        return dummy.next
        